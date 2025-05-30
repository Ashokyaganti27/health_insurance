# common functions using accross project

import os
import yaml
import joblib
import json
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from src.health_insurance import logger

# function for loading yaml file data

@ensure_annotations
def read_yaml(file_path) ->ConfigBox:
    
    try:
        with open(file_path) as yaml_file:
            # loading yaml
            file=yaml.safe_load(yaml_file)

            # configbox for working with dictionary data in easy and clean way like file.name unlike file[name]
            return ConfigBox(file)
    except FileNotFoundError:
        return "File is not found"
    except Exception as e:
        return e
    
# function for creating directories
@ensure_annotations
def create_directories(dir_paths: list, verbose=True):

    # accepting list of directories
    for path in dir_paths:
        os.makedirs(path,exist_ok=True)
        if verbose:
           logger.info(f"folder is created at: {path}")

# function for saving data to json
@ensure_annotations
def save_json(path:Path, data:dict):
    
    # opening file in write mode to write into file
    with open(path,"w") as file:
        json.dump(data,file,indent=4)

    logger.info(f"json file saved at {path}")

# function for loading json data
def load_json(path:Path)-> ConfigBox:
    
    # opeining file with read mode to read data from file
    with open(path, "r") as file :

        data =json.load(file)
    
    logger.info(f"json data successfully loaded at : {path}")
    
    return ConfigBox(data)

# function for saving model using joblib
@ensure_annotations
def save_model(data:Any, path:Path):

    # saving model

    joblib.dump(value=data,filename=path)
    logger.info(f"model successfully saved at {path}")

# function for loding model
def load_model(path:Path) ->Any:

    # loading model
    data=joblib.load(path)
    logger.info(f"model loaded from {path}")
    return data

