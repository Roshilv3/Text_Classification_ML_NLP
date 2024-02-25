from src.text_Classification_ML.constants import *
from src.text_Classification_ML.utils.common import *
from src.text_Classification_ML.entity import *



class ConfigurationManager:
    def __init__(
            self,
            config_file_path = Config_File_Path,
            params_file_path = Params_File_Path,
            schema_file_path = Schema_File_Path
            ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])


    ##############################################################################
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            sourceURL= config.sourceURL,
            local_file_dir= config.local_file_dir,
            unzip_dir= config.unzip_dir
        )


        return data_ingestion_config

    ##############################################################################
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.Columns

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            data_dir= config.data_dir,
            STATUS_FILE_DIR= config.STATUS_FILE_DIR,
            all_schema= schema
        )

        return data_validation_config
    
    ##############################################################################
    def get_data_cleaning_config(self) -> DataCleaningConfig:
        config = self.config.data_cleaning

        create_directories([config.root_dir])

        data_cleaning_config = DataCleaningConfig(
            root_dir= config.root_dir,
            data_dir= config.data_dir,
            new_data_dir= config.new_data_dir,
        )

        return data_cleaning_config
    
    ##############################################################################
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
                root_dir= config.root_dir,
                data_dir= config.data_dir
            )

        return data_transformation_config
    
    ##############################################################################
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_tfidf= config.train_tfidf,
            test_tfidf= config.test_tfidf,
            train_y= config.train_y,
            test_y= config.test_y,
            model_name= config.model_name
        )

        return model_trainer_config