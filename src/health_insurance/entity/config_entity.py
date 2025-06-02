
from dataclasses import dataclass
from pathlib import Path
@dataclass
class DataIngestonConfig:
    root_dir: Path
    dataset_name:str
    file_path_zip: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: Path
    all_schema: dict
    test_data_path:Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    test: Path
    train: Path