from src.text_Classification_ML.config.configuration import *
from src.text_Classification_ML.components.Model_evaluation import *

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config= model_evaluation_config)
        model_evaluation.save_results()