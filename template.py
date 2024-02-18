import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s:')

project_name = "text_Classification_ML"

Files_list = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "README.md",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in Files_list:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)


    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating file directory {file_dir} for the file {file_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file {filepath}")

    else:
        logging.info(f"{file_name} already exist")
