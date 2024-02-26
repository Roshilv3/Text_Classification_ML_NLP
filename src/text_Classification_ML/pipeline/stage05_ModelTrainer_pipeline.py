from src.text_Classification_ML.config.configuration import *
from src.text_Classification_ML.components.Model_Trainer import *
from src.text_Classification_ML.logger import logging

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config= model_trainer_config)
        model_trainer.train()
        logging.info("Model training successfully completed.")