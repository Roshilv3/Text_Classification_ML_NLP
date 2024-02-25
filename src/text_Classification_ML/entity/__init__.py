import os
from pathlib import Path
from dataclasses import dataclass

####################################
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    sourceURL: str
    local_file_dir: Path
    unzip_dir: Path

####################################
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_dir: Path
    STATUS_FILE_DIR: Path
    all_schema: dict

###################################
@dataclass(frozen=True)
class DataCleaningConfig:
    root_dir         : Path
    data_dir         : Path
    new_data_dir     : Path