from DigitDetection.constants import *
import os
import sys
from pathlib import Path
from DigitDetection.utils.common import read_yaml, create_directories
from DigitDetection.entity.config_entity import (DataIngestionConfig, 
                                                 DataPrepareConfig, 
                                                 BaseModelConfig)
from DigitDetection.logger import logging
from DigitDetection.exception import AppException

class ConfigurationManager:
    def __init__(self, 
    config_filepath = CONFIG_FILE_PATH, 
    params_filepath=PARAMS_FILE_PATH):

        try:
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            logging.info("Config and Params seted")

            create_directories([self.config.artifacts_root])
            logging.info("root_dir created")
        except Exception as e:
            raise AppException(e, sys)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:

            config = self.config.data_ingestion

            create_directories([config.root_dir])

            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir
            )
            return data_ingestion_config
            logging.info("data_ingestion_config returned")
        except Exception as e:
            raise AppException(e, sys)

    def get_data_prepare_config(self) -> DataPrepareConfig:
        try:
            config = self.config.data_prepare
            params = self.params

            data_prepare_config = DataPrepareConfig(
                train_images=config.train_images, 
                train_labels=config.train_labels, 
                test_images=config.test_images, 
                test_labels=config.test_labels, 
                batch_size=params.BATCH_SIZE, 
                image_shape=params.IMAGE_SHAPE
            )

            return data_prepare_config
        
        except Exception as e:
            raise AppException(e, sys)
    
    def get_base_model_config(self) -> BaseModelConfig:
        try:
            config = self.config.base_model
            params = self.params

            create_directories([config.root_dir])

            base_model_config = BaseModelConfig(
                root_dir=config.root_dir, 
                base_model_path=config.base_model_path, 
                image_shape=params.IMAGE_SHAPE
            )

            return base_model_config
        except Exception as e:
            raise AppException(e, sys)