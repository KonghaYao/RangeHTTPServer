# 使用官方的 Python 运行时作为父镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 安装所需的库
RUN pip install rangehttpserver

# 暴露端口
EXPOSE 8000

# 运行命令
CMD ["python", "-m", "RangeHTTPServer"]