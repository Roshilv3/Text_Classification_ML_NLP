import os
import pandas as pd
import scipy.sparse
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from src.text_Classification_ML.config.configuration import *
import warnings

warnings.filterwarnings("ignore")

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        data = pd.read_csv(self.config.data_dir)

        # Fill the missing values
        data['Cleaned_Review'].fillna("", inplace=True)

        # Re-Maping the rating volumn
        rating_map = {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}
        data['Rating'] = data['Rating'].map(rating_map)

        # Split the data into train and test sets.
        train, test = train_test_split(data, train_size=0.80)

        # Vectorize text using TF-IDF
        tfidf_vectorizer = TfidfVectorizer()
        train_tfidf = tfidf_vectorizer.fit_transform(train['Cleaned_Review'])
        test_tfidf = tfidf_vectorizer.transform(test['Cleaned_Review'])

        # Save the TF-IDF vectorizer
        vectorizer_filename = os.path.join(self.config.root_dir, "tfidf_vectorizer.pkl")
        joblib.dump(tfidf_vectorizer, vectorizer_filename)

        # Save the TF-IDF matrices
        train_tfidf_filename = os.path.join(self.config.root_dir, "train_tfidf.csv")
        test_tfidf_filename = os.path.join(self.config.root_dir, "test_tfidf.csv")
        scipy.sparse.save_npz(train_tfidf_filename, train_tfidf)
        scipy.sparse.save_npz(test_tfidf_filename, test_tfidf)

        # Save the train and test sets without text columns
        train = train.drop(columns=['Cleaned_Review'])
        test = test.drop(columns=['Cleaned_Review'])
        train_filename = os.path.join(self.config.root_dir, "train.csv")
        test_filename = os.path.join(self.config.root_dir, "test.csv")
        train.to_csv(train_filename, index=False)
        test.to_csv(test_filename, index=False)