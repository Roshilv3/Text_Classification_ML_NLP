from src.text_Classification_ML.config.configuration import *
from src.text_Classification_ML.components.Data_Cleaning import *


class DataCleaningPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_cleaning_config = config.get_data_cleaning_config()
        data_cleaning = DataCleaning(config=data_cleaning_config)
        data_cleaning.clean_text()
        data_cleaning.drop_columns_and_duplicates()
        data_cleaning.word_lemitization()
        data_cleaning.save_to_csv()