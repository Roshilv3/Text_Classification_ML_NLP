import pandas as pd
import joblib
import scipy.sparse
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from src.text_Classification_ML.logger import logging
from src.text_Classification_ML.utils.common import *
from src.text_Classification_ML.config.configuration import *



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def metrics_eval(self, actual, pred):
        accuracy = accuracy_score(actual, pred)
        precision = precision_score(actual, pred, average= "micro")
        recall = recall_score(actual, pred, average= "micro")
        f1 = f1_score(actual, pred, average= "micro")

        return accuracy, precision, recall, f1
    
    def save_results(self):
        test_tfidf = scipy.sparse.load_npz(self.config.test_tfidf)
        test_y = pd.read_csv(self.config.test_y)

        test_label = test_y['Rating']

        model = joblib.load(self.config.model_path)
        logging.info("Model loaded successfully")

        y_pred = model.predict(test_tfidf)

        (accuracy, precision,recall,f1) = self.metrics_eval(test_label, y_pred)

        scores = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        }

        save_json(path= Path(self.config.metrics_file_path), data= scores)
        logging.info("Result saved successfully")