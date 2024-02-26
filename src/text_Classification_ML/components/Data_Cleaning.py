import os
import pandas as pd
import emoji
import contractions
import re
import unicodedata
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from src.text_Classification_ML.logger import logging
from src.text_Classification_ML.config.configuration import DataCleaningConfig

nlp = spacy.load("en_core_web_sm")

class DataCleaning:
    def __init__(self, config: DataCleaningConfig):
        self.config = config
        self.stop_words = set(stopwords.words('english'))
        self.df = pd.read_csv(self.config.data_dir)
    
    def clean_text(self):
        self.df['Cleaned_Review'] = self.df['Review'].apply(self._clean_single_text)
        logging.info("text cleared")
        return self.df


    def _clean_single_text(self, text):
        text = emoji.demojize(text)  # fix emojis
        text = contractions.fix(text)  # fix contractions
        text = re.sub(r'[^\x00-\x7f]', r'', text)  # remove strange fonts
        text = re.sub(r"\d+", "number", text)  # replace numbers with "number"
        text = re.sub(r'[^\w\s]', '', text)  # remove non-alphanumeric chars
        text = text.replace('_', ' ')  # replace underscores with space
        text = re.sub(r'[^A-Z a-z 0-9-]+', '', text)
        text = text.strip()  # strip extra spaces
        text = text.lower()
        text = self._remove_accented_chars(text)  # remove accented characters
        text = self._remove_stop_words(text)  # remove stop words

        return text


    def _remove_accented_chars(self, text):
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        return text


    def _remove_stop_words(self, text):
        text_tokens = word_tokenize(text)
        filtered_tokens = [word for word in text_tokens if word.lower() not in self.stop_words]
        filtered_text = ' '.join(filtered_tokens)
        return filtered_text
    

    def drop_columns_and_duplicates(self):
        self.df.drop(columns=['Time_submitted','Total_thumbsup','Reply','Review'],inplace=True, axis=1)
        return self.df
    
    def word_lemitization(self):
        self.df['Cleaned_Review'] = self.df['Cleaned_Review'].apply(lambda x: ' '.join([token.lemma_ for token in nlp(x)]))
        return self.df
    
    
    def save_to_csv(self, filename= "data_spotify_new.csv"):
        filepath = os.path.join(self.config.new_data_dir, filename)
        self.df.to_csv(filepath, index=False)