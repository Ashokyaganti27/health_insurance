
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
    scaling: bool

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_path: Path
    model_name: str
    max_depth: 5
    min_samples_split: 4
    min_samples_leaf: 3