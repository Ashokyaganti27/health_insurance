
from dataclasses import dataclass
from pathlib import Path
@dataclass
class DataIngestonConfig:
    root_dir: Path
    dataset_name:str
    file_path_zip: Path