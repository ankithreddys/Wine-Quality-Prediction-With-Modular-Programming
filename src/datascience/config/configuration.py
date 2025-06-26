from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainingConfig



class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            data_file_csv=config.data_file_csv,
            STATUS_FILE=config.STATUS_FILE,
            all_schema = schema
        )

        return data_validation_config


    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        schema = self.schema.TARGET_COLUMN
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_file_csv = config.data_file_csv,
            schema=schema
        )

        return data_transformation_config
    
    def get_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        model_params = self.params.XGBOOST_PARAMS
        kf_params = self.params.KF_PARAMS
        cv_params = self.params.CV_PARAMS
        schema = self.schema.TARGET_COLUMN
        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            train_df_path=config.train_df_path,
            test_df_path=config.test_df_path,
            model_name=config.model_name,
            n_estimators=model_params.n_estimators,
            learning_rate=model_params.learning_rate,
            max_depth=model_params.max_depth,
            random_state=model_params.random_state,
            n_splits=kf_params.n_splits,
            shuffle=kf_params.shuffle,
            scoring=cv_params.scoring,
            n_jobs=cv_params.n_jobs,
            verbose=cv_params.verbose,
            schema=schema
        )
        
        return model_training_config

