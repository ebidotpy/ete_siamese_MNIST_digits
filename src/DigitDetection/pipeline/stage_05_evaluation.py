import sys
from DigitDetection.config.configuration import ConfigurationManager
from DigitDetection.components.evaluation import Evaluation
from DigitDetection.components.data_prepare import DataPrepare
from DigitDetection.logger import logging
from DigitDetection.exception import AppException

STAGE_NAME = "Evaluation Pipeline"
class EvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            confid = ConfigurationManager()
            eval_config = confid.get_evaluation_config()
            data_config = confid.get_data_prepare_config()

            evaluation = Evaluation(eval_config, data_config)
            evaluation.evaluation()
            evaluation.save_score()
        
        except Exception as e:
            raise AppException(e, sys)

try:
    if __name__ == "__main__":
        logging.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = EvaluationTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx====================================x")

except Exception as e:
    raise AppException(e, sys)