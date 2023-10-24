import os
import sys
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Lambda
from DigitDetection.entity.config_entity import BaseModelConfig
from DigitDetection.logger import logging
from DigitDetection.exception import AppException
from DigitDetection.utils.common import euclidean_distance

class BaseModel:
    def __init__(self, config: BaseModelConfig):
        try:
            self.config = config
        except Exception as e:
            raise AppException(e, sys)
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        try:
            model.save(path)

        except Exception as e:
            raise AppException(e, sys)
    
    def bild_siamese_model(self, embeddingDim=48):
        try:
            # specify the inputs for the feature extractor network
            inputs = Input(self.config.image_shape)

            # define the first set of CONV => RELU => POOL => DROPOUT layers
            x = Conv2D(64, (2, 2), padding="same", activation="relu")(inputs)
            x = MaxPooling2D(pool_size=(2, 2))(x)
            x = Dropout(0.3)(x)

            # second set of CONV => RELU => POOL => DROPOUT layers
            x = Conv2D(64, (2, 2), padding="same", activation="relu")(x)
            x = MaxPooling2D(pool_size=2)(x)
            x = Dropout(0.3)(x)

            # prepare the final outputs
            pooledOutput = GlobalAveragePooling2D()(x)
            outputs = Dense(embeddingDim)(pooledOutput)

            # build the model
            model = Model(inputs, outputs)
            
            return model
            
            

        except Exception as e:
            raise AppException(e, sys)
    
    def conjoin_sisters(self):
        try:
            imgA = Input(shape=self.config.image_shape)
            imgB = Input(shape=self.config.image_shape)

            featureExtractor = self.bild_siamese_model()

            featsA = featureExtractor(imgA)
            featsB = featureExtractor(imgB)

            distance = Lambda(euclidean_distance)([featsA, featsB])
            outputs = Dense(1, activation="sigmoid")(distance)
            model = Model(inputs=[imgA, imgB], outputs=outputs)

            model.compile(loss="binary_crossentropy", optimizer="adam", 
                    metrics=["accuracy"])
        
            self.save_model(path=self.config.base_model_path, model=model)
        except Exception as e:
            raise AppException(e, sys)

