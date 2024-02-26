from src.text_Classification_ML.config.configuration import *
from src.text_Classification_ML.components.Data_trasformation import *
from src.text_Classification_ML.logger import logging

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config= data_transformation_config)
        data_transformation.train_test_split()
        logging.info("Successfully converted the text data to tfidf vectors.")
        logging.info("Splitted the data form train and test.")