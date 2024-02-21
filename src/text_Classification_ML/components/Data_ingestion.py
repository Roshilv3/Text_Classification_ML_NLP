import os
from urllib import request
import zipfile
from src.text_Classification_ML.logger import logging
from src.text_Classification_ML.entity import *



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_data(self):
        if not os.path.exists(self.config.local_file_dir):
            filename, headers = request.urlretrieve(
                url= self.config.sourceURL,
                filename= self.config.local_file_dir
                )
            logging.info(f"{filename} download! with following info: \n{headers}")
        else:
            logging.info(f"{filename} already exist")


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_file_dir, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  