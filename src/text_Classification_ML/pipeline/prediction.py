from src.text_Classification_ML.utils.common import load_object
import joblib



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load("artifacts/model_trainer/model.joblib")

    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction