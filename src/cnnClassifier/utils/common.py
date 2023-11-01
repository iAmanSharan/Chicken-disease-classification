import os
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from typing import Any
import base64
from pathlib  import Path
import joblib
import json
import yaml
from box  import ConfigBox
from  cnnClassifier import logger


@ensure_annotations
def read_yaml(path_to_file:Path)->ConfigBox:
  """
  Reads a yaml file and returns a ConfigBox object.
  """
  try:
    path_to_file = Path(path_to_file)
    logger.info(f"Reading yaml file from {path_to_file}")
    with open(path_to_file, "r") as f:
        yaml_file = yaml.safe_load(f)
    return ConfigBox(yaml_file)
  except BoxValueError:
    raise ValueError("yaml file is empty")
  except Exception as e:
     return e
  
@ensure_annotations
def create_directories(path_to_dir:Path):
    """
    Creates a directory if it does not exist.
    """
    try:
        path_to_dir = Path(path_to_dir)
        logger.info(f"Creating directory at {path_to_dir}")
        if not os.path.exists(path_to_dir):
            os.makedirs(path_to_dir)
    except Exception as e:
        return e
    
@ensure_annotations
def json_file(filepath:Path, data:dict):
   try:
      with open(filepath , "w") as f:
         json.dump('data', f  , indent=4)
      logger.info("json file saved")

   except Exception as e:
      return e

@ensure_annotations
def load_json(path:Path)->ConfigBox:
   with open(path,"w") as f:
     logger.info("Json File loaded")