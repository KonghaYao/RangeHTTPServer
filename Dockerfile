# 使用官方的 Python 运行时作为父镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

COPY server/ /app/server/

COPY main.py /app/main.py
# 暴露端口
EXPOSE 8000

# 运行命令
CMD ["python", "main.py"]