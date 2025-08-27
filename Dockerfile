# 使用官方的 Python 运行时作为父镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

COPY pyproject.toml /app/pyproject.toml

COPY server/__init__.py /app/server/__init__.py

COPY main.py /app/main.py

COPY *.html /app/

# 暴露端口
EXPOSE 8000

# 运行命令
CMD ["python", "main.py", "8000"]