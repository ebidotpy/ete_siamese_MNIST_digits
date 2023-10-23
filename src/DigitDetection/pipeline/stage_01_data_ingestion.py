import sys
from DigitDetection.config.configuration import ConfigurationManager
from DigitDetection.components.data_ingestion import DataIngestion
from DigitDetection.logger import logging
from DigitDetection.exception import AppException

STAGE_NAME = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            logging.info(f"{STAGE_NAME} pipeline created")
        
        except Exception as e:
            raise AppException(e, sys)

try:
    if __name__ == "__main__":
            logging.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
            obj = DataIngestionTrainingPipeline()
            obj.main()
            logging.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<\n\nx=======================================x")
except Exception as e:
    raise AppException(e, sys)