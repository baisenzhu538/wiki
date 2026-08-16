@echo off
rem KDO MCP Server launcher - clears PYTHONPATH pollution from Hermes venv
rem The Hermes session exports PYTHONPATH pointing at its cp313 venv,
rem which breaks Python312's pydantic_core (cp312 binary required).
set PYTHONPATH=
"C:\Program Files\Python312\python.exe" "C:\Users\Administrator\Desktop\wiki\kdo-tools\mcp\server.py" %*
