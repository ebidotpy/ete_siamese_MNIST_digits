import os
import sys
from DigitDetection.components.data_prepare import DataPrepare
from DigitDetection.config.configuration import ConfigurationManager
from DigitDetection.logger import logging
from DigitDetection.exception import AppException

SATGE_NAME = "Data Prepare Pipeline"

class DataPrepareTrainPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            data_prepare_config = config.get_data_prepare_config()
            data_prepare = DataPrepare(data_prepare_config)
            data_prepare.get_data()

        except Exception as e:
            raise AppException(e, sys)

try:
    logging.info(f">>>>>>>>>>>> stage {SATGE_NAME} started <<<<<<<<<<<<<<<<<<")
    obj = DataPrepareTrainPipeline()
    obj.main()
    logging.info(f">>>>>>>>>>>> stage {SATGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx==================================================x")

except Exception as e:
    raise AppException(e, sys)
