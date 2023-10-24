import sys
from DigitDetection.components.training import Training
from DigitDetection.config.configuration import ConfigurationManager
from DigitDetection.logger import logging
from DigitDetection.exception import AppException

STAGE_NAME = "Training Pipeline"

class TrainingPipline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            data_config = config.get_data_prepare_config()
            training = Training(data_config, training_config)
            training.training()
        except Exception as e:
            raise AppException(e, sys)

try:
    if __name__ == "__main__":
        logging.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        obj = TrainingPipline()
        obj.main()
        logging.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx=============================================x")

except Exception as e:
    raise AppException(e, sys)