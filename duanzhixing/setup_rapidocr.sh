#!/bin/bash
# RapidOCR 一键安装脚本
# 运行前请确保网络通畅（模型文件约 15-30MB）
# 执行: bash setup_rapidocr.sh

set -e

echo "=== RapidOCR 安装脚本 ==="
echo ""

# 检查是否在 venv 中
if [ -z "$VIRTUAL_ENV" ]; then
    echo "[*] 激活虚拟环境..."
    source /home/dministrator/.hermes/hermes-agent/venv/bin/activate
fi

# 1. 确保 pip 可用
python3 -m ensurepip --upgrade >/dev/null 2>&1

# 2. 安装 rapidocr（包含模型文件）
echo "[*] 安装 rapidocr 主包（含模型文件，约 15-30MB）..."
python3 -m pip install rapidocr --no-cache-dir --timeout 600 -i https://pypi.tuna.tsinghua.edu.cn/simple

# 3. 验证安装
echo "[*] 验证安装..."
python3 -c "
from rapidocr import RapidOCR
engine = RapidOCR()
print('✅ RapidOCR 安装成功，模型加载正常')
"

echo ""
echo "=== 安装完成 ==="
echo "使用方式: from rapidocr import RapidOCR"
