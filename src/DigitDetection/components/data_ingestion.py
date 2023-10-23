import os
from DigitDetection.logger import logging
from DigitDetection.exception import AppException
from DigitDetection.entity.config_entity import DataIngestionConfig
from pathlib import Path
import tensorflow as tf

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):

        # Download the MNIST dataset
        mnist = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        # Create a directory to save the dataset
        import os
        if not os.path.exists(self.config.root_dir):
            os.makedirs(self.config.root_dir)

        # Save the training and test sets as separate files in the MNIST directory
        with open(f"{self.config.root_dir}/train-images-idx3-ubyte", "wb") as f:
            f.write(x_train.tobytes())
        with open(f"{self.config.root_dir}/train-labels-idx1-ubyte", "wb") as f:
            f.write(y_train.tobytes())
        with open(f"{self.config.root_dir}/t10k-images-idx3-ubyte", "wb") as f:
            f.write(x_test.tobytes())
        with open(f"{self.config.root_dir}/t10k-labels-idx1-ubyte", "wb") as f:
            f.write(y_test.tobytes())

