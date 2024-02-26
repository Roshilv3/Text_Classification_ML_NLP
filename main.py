from src.text_Classification_ML.logger import logging
from src.text_Classification_ML.pipeline.stage01_DataIngestion_pipeline import *
from src.text_Classification_ML.pipeline.stage02_DataValidation_pipeline import *
from src.text_Classification_ML.pipeline.Stage03_DataCleaning_pipeline import *
from src.text_Classification_ML.pipeline.stage04_DataTransformation_pipeline import *
from src.text_Classification_ML.pipeline.stage05_ModelTrainer_pipeline import *
from src.text_Classification_ML.pipeline.stage06_ModelEvaluation_pipeline import *


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

###########################################################################
STAGE_NAME_03 = "DATA CLEANING STAGE"
try:
    logging.info(f">>> {STAGE_NAME_03} started<<<")
    data_cleaning = DataCleaningPipeline()
    data_cleaning.main()
    logging.info(f">>> {STAGE_NAME_03} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

###########################################################################
STAGE_NAME_04 = "DATA TRANSFORMATION STAGE"
try:
    logging.info(f">>> {STAGE_NAME_04} started<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logging.info(f">>> {STAGE_NAME_04} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

###########################################################################
STAGE_NAME_05 = "MODEL TRAINER STAGE"
try:
    logging.info(f">>> {STAGE_NAME_05} started<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logging.info(f">>> {STAGE_NAME_05} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e

###########################################################################
STAGE_NAME_06 = "MODEL EVALUATION STAGE"
try:
    logging.info(f">>> {STAGE_NAME_06} started<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logging.info(f">>> {STAGE_NAME_06} completed<<<\n\n -_-_-_-_-_-")
except Exception as e:
    raise e