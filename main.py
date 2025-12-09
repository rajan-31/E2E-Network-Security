from src.NetworkSecurity.logging.logger import logger
from src.NetworkSecurity.utils.common import read_yaml


logger.info("Logger is initialized")

config = read_yaml("config/config.yaml")
print(config)