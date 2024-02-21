from src.text_Classification_ML.entity import *
from src.text_Classification_ML.config.configuration import *
from src.text_Classification_ML.components.Data_ingestion import *


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config= data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()