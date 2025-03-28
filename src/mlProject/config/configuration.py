from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import (
    DataIngestionConfig, DataValidationConfig, ModelEvaluationConfig, 
    DataTransformationConfig, ModelTrainerConfig
)

class ConfigurationManager:
    def __init__(self, 
                 config_filepath=CONFIG_FILE_PATH, 
                 params_filepath=PARAMS_FILE_PATH, 
                 schema_filepath=SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config["artifacts_root"]])  # Correct key access

    # Data Ingestion Configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]
        create_directories([config["root_dir"]])

        return DataIngestionConfig(
            root_dir=config["root_dir"],
            source_URL=config["source_URL"],
            local_data_file=config["local_data_file"],
            unzip_dir=config["unzip_dir"]
        )

    # Data Validation Configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config["data_validation"]
        schema = self.schema["COLUMNS"]
        create_directories([config["root_dir"]])

        return DataValidationConfig(
            root_dir=config["root_dir"],
            STATUS_FILE=config["STATUS_FILE"],
            unzip_data_dir=config["unzip_data_dir"],
            all_schema=schema,
        )

    # Data Transformation Configuration
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config["data_transformation"]
        create_directories([config["root_dir"]])

        return DataTransformationConfig(
            root_dir=config["root_dir"],
            data_path=config["data_path"]
        )

    # Model Trainer Configuration
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config["model_trainer"]
        model_params = self.params["best_hyperparameters"]
        model_name_config = self.params["model_name"]
        target_column_name = self.schema["TARGET_COLUMN"]["name"]

        create_directories([config["root_dir"]])

        return ModelTrainerConfig(
            root_dir=config["root_dir"],
            train_data_path=config["train_data_path"],
            test_data_path=config["test_data_path"],
            model_name=model_name_config["name"],
            random_state=model_name_config["random_state"],
            n_estimators=model_params["n_estimators"],
            min_samples_split=model_params["min_samples_split"],
            min_samples_leaf=model_params["min_samples_leaf"],
            max_features=model_params["max_features"],
            max_depth=model_params["max_depth"],
            bootstrap=model_params["bootstrap"],
            target_column=target_column_name
        )

    # Model Evaluation Configuration
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config["model_evaluation"]
        model_params = self.params["best_hyperparameters"]
        model_name = self.params["model_name"]["name"]
        target_column_name = self.schema["TARGET_COLUMN"]["name"]

        create_directories([config["root_dir"]])

        return ModelEvaluationConfig(
            root_dir=config["root_dir"],
            test_data_path=config["test_data_path"],
            model_path=config["model_path"],
            all_params=model_params,
            metric_file_name=config["metric_file_name"],
            target_column=target_column_name
        )
