import os 
from pathlib import Path
os.environ["KAGGLE_CONFIG_DIR"] = os.path.join(os.getcwd(), ".kaggle")

CONFIG_FILE_PATH=Path("config/config.yaml")
PARAMS_FILE_PATH=Path("params.yaml")
SCHEMA_FILE_PATH=Path("schema.yaml")

