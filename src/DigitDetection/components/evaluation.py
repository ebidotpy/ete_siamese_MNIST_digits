import sys
import os
from pathlib import Path
import tensorflow as tf
from DigitDetection.entity.config_entity import (EvaluationConfig, 
                                                 DataPrepareConfig)
from DigitDetection.components.data_prepare import DataPrepare
from DigitDetection.logger import logging
from DigitDetection.exception import AppException
from DigitDetection.utils.common import save_json

class Evaluation:
    def __init__(self, eval_config: EvaluationConfig, data_config: DataPrepareConfig):
        try:
            self.eval_config = eval_config
            self.data_config = data_config

        except Exception as e:
            raise AppException(e, sys)
    
    def fetch_data(self):
        try:
            data = DataPrepare(self.data_config)
            train, test = data.get_data()
            (pairTrain, labelTrain) = train
            (pairTest, labelTest) = test
            return (pairTrain, labelTrain), (pairTest, labelTest)
        except Exception as e:
            raise AppException(e, sys)
    def evaluation(self):
        try:
            _, test = self.fetch_data()
            (pairTest, labelTest) = test
            model = tf.keras.models.load_model(self.eval_config.trained_model_path)
            self.score = model.evaluate([pairTest[:, 0], pairTest[:, 1]], labelTest[:])

        except Exception as e:
            raise AppException(e, sys)
    def save_score(self):
        try:
            scores = {"loss": self.score[0], "accuracy": self.score[1]}
            save_json(path=Path(os.path.join(self.eval_config.root_dir+"/"+"scores.json")), data=scores)
        except Exception as e:
            raise AppException(e, sys)