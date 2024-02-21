from src.text_Classification_ML.logger import logging
from src.text_Classification_ML.pipeline.stage01_DataIngestion_pipeline import *
from src.text_Classification_ML.pipeline.stage02_DataValidation_pipeline import *


############################################################################
STAGE_NAME_01 = "DATA INGESTION STAGE"
try:
    logging.info(f">>> {STAGE_NAME_01} started<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f">>> {STAGE_NAME_01} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

###########################################################################
STAGE_NAME_02 = "DATA VALIDATION STAGE"
try:
    logging.info(f">>> {STAGE_NAME_02} started<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logging.info(f">>> {STAGE_NAME_02} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e