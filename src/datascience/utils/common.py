import os
import yaml
import json
import joblib
from src.datascience import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loded successfully")
            return ConfigBox(content)
    
    except Exception as e:
        raise e 


@ensure_annotations
def create_directories(path_to_directories: list):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info("Directory for path: {path} created")


@ensure_annotations
def save_json(path_to_save_json: Path, data: dict):
    with open(path_to_save_json, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at : {path_to_save_json}")


@ensure_annotations
def load_json(path_to_json_file:Path):
    with open(path_to_json_file,"r") as f:
        json_data = ConfigBox(json.load(f))
    logger.info(f"json file loaded from : {path_to_json_file}")
    return json_data


@ensure_annotations
def save_bin(data, path: Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file saved at {path}")    


@ensure_annotations
def load_bindata(path_to_bin_file:Path):
    data = joblib.load(filename=path_to_bin_file)
    logger.info(f"Binary data loaded from : {path_to_bin_file}")
    return data