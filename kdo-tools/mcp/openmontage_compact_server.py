"""Compact OpenMontage MCP stdio server for Hermes.

Why this exists
---------------
The upstream openmontage_mcp.server exposes *every* registered raw tool
directly in tools/list. That produces a >100KB single-line tools/list
payload which trips the Hermes venv's MCP 2.x stdio client (list_tools
hangs until the 120s discovery timeout).

This wrapper keeps the same OpenMontage registry / tool adapter / job
tracker and the same call_tool semantics, but only advertises the six
high-level entry points. The generic ``run_tool`` + ``list_capabilities``
pair still gives full access to every OpenMontage tool by name, so no
capability is lost. The KDO/openmontage repo itself is left untouched.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys

# #350 UTF-8 修复（#323 同款）：Windows 中文环境管道默认 cp936，UTF-8 JSON 必乱码
sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from pathlib import Path
from typing import Any

PROJECT_ROOT = r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\tools\openmontage-zh-mcp"

# Resolve project dir before importing OpenMontage modules so .env discovery
# and relative paths (pipeline/, styles/, etc.) resolve exactly like upstream.
def _resolve_project_dir(requested: Path | None) -> Path:
    project = (requested or Path(PROJECT_ROOT)).resolve()
    os.chdir(project)
    if project.as_posix() not in sys.path:
        sys.path.insert(0, str(project))
    return project


def _import_openmontage():
    from openmontage_mcp.server import _import_openmontage as upstream_import
    return upstream_import()


def _build_server(project_dir: Path):
    registry, ToolResult, tool_result_to_mcp_contents, tool_to_mcp, validate_inputs, tracker = _import_openmontage()
    registry.discover()

    from mcp.server import Server
    from mcp.types import TextContent, Tool

    server = Server("openmontage-compact")

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="list_capabilities",
                description="List available OpenMontage tools, runtimes, and setup offers.",
                inputSchema={"type": "object", "properties": {}},
            ),
            Tool(
                name="run_tool",
                description=(
                    "Execute any OpenMontage tool by name with a JSON inputs object. "
                    "Use list_capabilities to discover tool names and schemas."
                ),
                inputSchema={
                    "type": "object",
                    "required": ["name", "inputs"],
                    "properties": {
                        "name": {"type": "string", "description": "Tool name"},
                        "inputs": {"type": "object", "description": "Tool inputs"},
                        "defer": {"type": "boolean", "default": False, "description": "If true, run in background and return a job_id"},
                    },
                },
            ),
            Tool(
                name="render_video",
                description="Render a video from edit_decisions and an asset_manifest using Remotion, HyperFrames, or FFmpeg. Returns a job_id for polling.",
                inputSchema={
                    "type": "object",
                    "required": ["edit_decisions", "asset_manifest"],
                    "properties": {
                        "edit_decisions": {"type": "object"},
                        "asset_manifest": {"type": "object"},
                        "output_path": {"type": "string"},
                        "profile": {"type": "string"},
                        "audio_path": {"type": "string"},
                        "subtitle_path": {"type": "string"},
                    },
                },
            ),
            Tool(
                name="run_pipeline_stage",
                description="Write a checkpoint for a pipeline stage, advancing project state.",
                inputSchema={
                    "type": "object",
                    "required": ["project_id", "pipeline_type", "stage", "status", "artifacts"],
                    "properties": {
                        "project_id": {"type": "string"},
                        "pipeline_type": {"type": "string"},
                        "stage": {"type": "string"},
                        "status": {"type": "string", "enum": ["completed", "awaiting_human", "in_progress", "failed"]},
                        "artifacts": {"type": "object"},
                        "human_approval_required": {"type": "boolean", "default": False},
                        "human_approved": {"type": "boolean", "default": False},
                    },
                },
            ),
            Tool(
                name="get_pipeline_status",
                description="Query completed stages and next stage for a project/pipeline.",
                inputSchema={
                    "type": "object",
                    "required": ["project_id", "pipeline_type"],
                    "properties": {
                        "project_id": {"type": "string"},
                        "pipeline_type": {"type": "string"},
                    },
                },
            ),
            Tool(
                name="get_job_status",
                description="Poll the status of a deferred render or run_tool job.",
                inputSchema={
                    "type": "object",
                    "required": ["job_id"],
                    "properties": {"job_id": {"type": "string"}},
                },
            ),
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any] | None) -> list[TextContent]:
        arguments = arguments or {}

        if name == "list_capabilities":
            summary = registry.provider_menu_summary()
            return [TextContent(type="text", text=json.dumps(summary, indent=2))]

        if name == "get_job_status":
            job_id = arguments.get("job_id", "")
            state = tracker.get(job_id)
            if state is None:
                return [TextContent(type="text", text=json.dumps({"error": f"job {job_id} not found"}, indent=2))]
            return [TextContent(type="text", text=json.dumps(state, indent=2))]

        if name == "run_tool":
            tool_name = arguments.get("name", "")
            inputs = arguments.get("inputs", {})
            defer = arguments.get("defer", False)
            tool = registry.get(tool_name)
            if tool is None:
                return [TextContent(type="text", text=json.dumps({"error": f"tool {tool_name} not found"}, indent=2))]
            try:
                validate_inputs(tool, inputs)
            except Exception as exc:
                return [TextContent(type="text", text=json.dumps({"error": f"input validation failed: {exc}"}, indent=2))]

            if defer:
                job_id = tracker.submit(lambda: tool.execute(inputs))
                return [TextContent(type="text", text=json.dumps({"job_id": job_id, "status": "pending"}, indent=2))]

            result = tool.execute(inputs)
            return tool_result_to_mcp_contents(result)

        if name == "render_video":
            tool = registry.get("video_compose")
            if tool is None:
                return [TextContent(type="text", text=json.dumps({"error": "video_compose tool not found"}, indent=2))]
            inputs = {
                "operation": "render",
                "edit_decisions": arguments.get("edit_decisions"),
                "asset_manifest": arguments.get("asset_manifest"),
            }
            for key in ("output_path", "profile", "audio_path", "subtitle_path"):
                if key in arguments:
                    inputs[key] = arguments[key]
            job_id = tracker.submit(lambda: tool.execute(inputs))
            return [TextContent(type="text", text=json.dumps({"job_id": job_id, "status": "pending"}, indent=2))]

        if name == "run_pipeline_stage":
            from openmontage_mcp.pipeline_adapter import PipelineAdapter
            adapter = PipelineAdapter(project_dir)
            try:
                result = adapter.write_stage_checkpoint(
                    project_id=arguments["project_id"],
                    pipeline_type=arguments["pipeline_type"],
                    stage=arguments["stage"],
                    status=arguments["status"],
                    artifacts=arguments["artifacts"],
                    human_approval_required=arguments.get("human_approval_required", False),
                    human_approved=arguments.get("human_approved", False),
                )
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            except Exception as exc:
                return [TextContent(type="text", text=json.dumps({"error": str(exc)}, indent=2))]

        if name == "get_pipeline_status":
            from openmontage_mcp.pipeline_adapter import PipelineAdapter
            adapter = PipelineAdapter(project_dir)
            try:
                status = adapter.get_status(arguments["project_id"], arguments["pipeline_type"])
                return [TextContent(type="text", text=json.dumps(status, indent=2))]
            except Exception as exc:
                return [TextContent(type="text", text=json.dumps({"error": str(exc)}, indent=2))]

        # Fallback: allow direct calls to named OpenMontage tools when known.
        tool = registry.get(name)
        if tool is not None:
            try:
                validate_inputs(tool, arguments)
            except Exception as exc:
                return [TextContent(type="text", text=json.dumps({"error": f"input validation failed: {exc}"}, indent=2))]
            result = tool.execute(arguments)
            return tool_result_to_mcp_contents(result)

        return [TextContent(type="text", text=json.dumps({"error": f"unknown tool: {name}"}, indent=2))]

    return server


def main() -> int:
    parser = argparse.ArgumentParser(description="OpenMontage Compact MCP Server (Hermes)")
    parser.add_argument("--project-dir", type=Path, default=None, help="OpenMontage project root")
    args = parser.parse_args()

    project_dir = _resolve_project_dir(args.project_dir)
    if not (project_dir / "config.yaml").exists():
        print(f"Warning: {project_dir} does not look like an OpenMontage project (config.yaml not found).", file=sys.stderr)

    server = _build_server(project_dir)

    async def _run() -> None:
        from mcp.server.stdio import stdio_server
        async with stdio_server() as (read_stream, write_stream):
            await server.run(read_stream, write_stream, server.create_initialization_options())

    asyncio.run(_run())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())