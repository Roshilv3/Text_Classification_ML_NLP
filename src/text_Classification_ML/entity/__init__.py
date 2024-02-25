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

####################################
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_dir: Path

####################################
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_tfidf: Path
    test_tfidf: Path
    train_y: Path
    test_y: Path
    model_name: str
