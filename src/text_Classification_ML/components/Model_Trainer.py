import pandas as pd
import scipy.sparse
import joblib
from sklearn.linear_model import LogisticRegression
from src.text_Classification_ML.config.configuration import *

class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config = config


    def train(self):
        # load the matrix
        train_tfidf = scipy.sparse.load_npz(self.config.train_tfidf)
        test_tfidf = scipy.sparse.load_npz(self.config.test_tfidf)
        train = pd.read_csv(self.config.train_y)
        test = pd.read_csv(self.config.test_y)

        # Train a Logistic Regression model
        model = LogisticRegression(max_iter=1000)
        model.fit(train_tfidf, train['Rating'])

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))