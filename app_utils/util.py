import yaml
import os,sys
from app_exception.exception import AppException
from app_logger.logger import logging

def read_yaml_file(config_file_path:str)->dict:
    try:
        logging.info("Reading the configuration file")
        with open(config_file_path,"rb") as config_file:
            config_dict = yaml.safe_load(config_file)
            logging.info("Configuration file read successfully")
            return config_dict
    except Exception as e:
        raise AppException(e,sys) from e    