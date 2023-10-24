import sys
from DigitDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from DigitDetection.pipeline.stage_02_data_prepare import DataPrepareTrainPipeline
from DigitDetection.pipeline.stage_03_prepare_base_model import BaseModelTrainingPipeline
from DigitDetection.pipeline.stage_04_training import TrainingPipline
from DigitDetection.pipeline.stage_05_evaluation import EvaluationTrainingPipeline
from DigitDetection.logger import logging
from DigitDetection.exception import AppException

STAGE_NAME = "Data Ingestion Pipeline"
try:
    if __name__ == "__main__":
            logging.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
            obj = DataIngestionTrainingPipeline()
            obj.main()
            logging.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<\n\nx=======================================x")
except Exception as e:
    raise AppException(e, sys)

STAGE_NAME = "Data Prepare Pipeline"
try:
    logging.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<")
    obj = DataPrepareTrainPipeline()
    obj.main()
    logging.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx==================================================x")

except Exception as e:
    raise AppException(e, sys)


STAGE_NAME = "Prepare Base Model Pipeline"
try:
    if __name__ == "__main__":
        logging.info(f">>>>>>>>>>>> stage {STAGE_NAME} atarted <<<<<<<<<<<<<<<<<<")
        obj = BaseModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx==============================================x")


except Exception as e:
    raise AppException(e, sys)


STAGE_NAME = "Training Pipeline"
try:
    if __name__ == "__main__":
        logging.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        obj = TrainingPipline()
        obj.main()
        logging.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx=============================================x")

except Exception as e:
    raise AppException(e, sys)

STAGE_NAME = "Evaluation Pipeline"
try:
    if __name__ == "__main__":
        logging.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = EvaluationTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx====================================x")

except Exception as e:
    raise AppException(e, sys)