import os
import sys
from DigitDetection.components.base_model import BaseModel
from DigitDetection.config.configuration import ConfigurationManager
from DigitDetection.logger import logging
from DigitDetection.exception import AppException

STAGE_NAME = "Prepare Base Model"

class BaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            base_model_config = config.get_base_model_config()
            base_model = BaseModel(base_model_config)
            base_model.conjoin_sisters()

        except Exception as e:
            raise AppException(e, sys)

try:
    if __name__ == "__main__":
        logging.info(f">>>>>>>>>>>> stage {STAGE_NAME} atarted <<<<<<<<<<<<<<<<<<")
        obj = BaseModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx==============================================x")


except Exception as e:
    raise AppException(e, sys)