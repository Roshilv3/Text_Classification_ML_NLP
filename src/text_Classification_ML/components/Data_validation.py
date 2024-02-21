import pandas as pd
from src.text_Classification_ML.config.configuration import *
from src.text_Classification_ML.logger import logging




class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.data_dir)
            columns = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in columns:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE_DIR, "w") as f:
                        f.write(f"Validation_Status: {validation_status} \n\nALL COLUMNS ARE NOT MATCHED")

                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE_DIR, "w") as f:
                        f.write(f"Validation_Status: {validation_status} \n\nALL COLUMNS ARE MATCHED")

            logging.info(f"validaiton status is {validation_status}")
            return validation_status


        except Exception as e:
            raise e