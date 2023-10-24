import sys
import os
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Lambda
from tensorflow.keras.datasets import mnist
import numpy as np
from DigitDetection.entity.config_entity import (TrainingConfig,
                                                 DataPrepareConfig)
from DigitDetection.components.data_prepare import DataPrepare
from DigitDetection.logger import logging
from DigitDetection.exception import AppException

class Training:
    def __init__(self, data_prepare_config: DataPrepareConfig, training_config: TrainingConfig):
        try:
            self.data_config = data_prepare_config
            self.training_config = training_config
        
        except Exception as e:
            raise AppException(e, sys)
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        try:
            model.save(path)

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
    def training(self):
        try:
            model = tf.keras.models.load_model(self.training_config.base_model_path)
            (pairTrain, labelTrain), (pairTest, labelTest) = self.fetch_data()
            history = model.fit(
                [pairTrain[:, 0], pairTrain[:, 1]], labelTrain[:], 
                validation_data = ([pairTest[:, 0], pairTest[:, 1]], labelTest[:]), 
                batch_size=self.training_config.batch_size, 
                epochs=self.training_config.epochs
            )
            self.save_model(path=self.training_config.trained_model_path, model=model)

        except Exception as e:
            raise AppException(e, sys)

        
