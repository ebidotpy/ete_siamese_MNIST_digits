import tensorflow as tf
import sys
import os
import numpy as np
from DigitDetection.entity.config_entity import DataPrepareConfig
from DigitDetection.logger import logging
from DigitDetection.exception import AppException

class DataPrepare:
    def __init__(self, config: DataPrepareConfig):
        try:
            self.config = config

        except Exception as e:
            raise AppException(e, sys)

    # Create a function to parse the MNIST dataset files
    def parse_mnist(self, image_file, label_file):
        try:
            image = tf.io.decode_raw(tf.io.read_file(image_file), tf.uint8)
            image = tf.reshape(image, [-1, 28, 28, 1])
            image = tf.cast(image, tf.float32) / 255.0

            label = tf.io.decode_raw(tf.io.read_file(label_file), tf.uint8)
            label = tf.reshape(label, [-1])
            label = tf.cast(label, tf.int32)

            return image, label
        except Exception as e:
            raise AppException(e, sys)
    
    def make_pairs(self, images, labels):
        try:

            # initialize two empty lists to hold the (image, image) pairs and
            # labels to indicate if a pair is positive or negative
            pairImages = []
            pairLabels = []

            # calculate the total number of classes present in the dataset
            # and then build a list of indexes for each class label that
            # provides the indexes for all examples with a given label
            numClasses = len(np.unique(labels))
            idx = [np.where(labels == i)[0] for i in range(0, numClasses)]

            # loop over all images
            for idxA in range(len(images)):
                # grab the current image and label belonging to the current
                # iteration
                currentImage = images[idxA]
                label = labels[idxA]

                # randomly pick an image that belongs to the *same* class
                # label
                idxB = np.random.choice(idx[label])
                posImage = images[idxB]

                # prepare a positive pair and update the images and labels
                # lists, respectively
                pairImages.append([currentImage, posImage])
                pairLabels.append([1])

                # grab the indices for each of the class labels *not* equal to
                # the current label and randomly pick an image corresponding
                # to a label *not* equal to the current label
                negIdx = np.where(labels != label)[0]
                negImage = images[np.random.choice(negIdx)]

                # prepare a negative pair of images and update our lists
                pairImages.append([currentImage, negImage])
                pairLabels.append([0])

            # return a 2-tuple of our image pairs and labels
            return (np.array(pairImages), np.array(pairLabels))
        except Exception as e:
            raise AppException(e, sys)
    def get_data(self):
        try:
            train_images_file = self.config.train_images
            train_labels_file = self.config.train_labels
            test_images_file = self.config.test_images
            test_labels_file = self.config.test_labels
            if os.path.exists(train_images_file):
                train_images, train_labels = self.parse_mnist(train_images_file, train_labels_file)
                test_images, test_labels = self.parse_mnist(test_images_file, test_labels_file)

                train = self.make_pairs(train_images, train_labels)
                test = self.make_pairs(test_images, test_labels)
                
                return train, test

        except Exception as e:
            raise AppException(e, sys)
