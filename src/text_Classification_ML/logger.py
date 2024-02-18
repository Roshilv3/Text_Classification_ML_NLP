import os
import sys
import logging
from datetime import datetime

log_str = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"log",log_str)
os.makedirs(log_path, exist_ok=True)

Log_file_path = os.path.join(log_path,log_str)

logging.basicConfig(
    filename = Log_file_path,
    format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]",
    level= logging.INFO
)