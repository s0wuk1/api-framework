import logging
import os
# 创建日志器
logger = logging.getLogger()
# 设置日志级别
logger.setLevel(logging.INFO)
# 日志输出格式
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
# 创建文件处理器
# os.makedirs("../logs", exist_ok=True)
file_handler = logging.FileHandler(
    "../logs/test.log",
    encoding="utf-8"
)
# 设置格式
file_handler.setFormatter(formatter)
# 创建控制台处理器
console_handler = logging.StreamHandler()
# 设置格式
console_handler.setFormatter(formatter)

# 添加处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)