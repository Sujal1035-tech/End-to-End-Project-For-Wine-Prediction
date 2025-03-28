from mlProject.constants import *
from mlProject.utils.common import read_yaml,create_directories
from mlProject.entity.config_entity import (DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig )
#data_ingestion
class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH ):

            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            self.schema = read_yaml(schema_filepath)

            create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    #data validation
    class ConfigurationManager:
        def __init__(
         self,
         config_filepath = CONFIG_FILE_PATH,
         params_filepath = PARAMS_FILE_PATH,
         schema_filepath = SCHEMA_FILE_PATH):

         self.config = read_yaml(config_filepath)
         self.params = read_yaml(params_filepath)
         self.schema = read_yaml(schema_filepath)

         create_directories([self.config.artifacts_root])


    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    

    #data transformation
    class ConfigurationManager:
     def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    

    class ConfigurationManager:
     def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_model_trainer_config(self) -> ModelTrainerConfig:
     config = self.config.model_trainer
     model_params = self.params.best_hyperparameters
     model_name_config = self.params.model_name
     target_column_name = self.schema.TARGET_COLUMN.name

     create_directories([config.root_dir])

     model_trainer_config = ModelTrainerConfig(
        root_dir=config.root_dir,
        train_data_path=config.train_data_path,
        test_data_path=config.test_data_path,
        model_name=model_name_config.name,  # "RandomForestRegressor"
        random_state=model_name_config.random_state,  # 42
        n_estimators=model_params.n_estimators,  # 400
        min_samples_split=model_params.min_samples_split,  # 10
        min_samples_leaf=model_params.min_samples_leaf,  # 2
        max_features=model_params.max_features,  # "log2"
        max_depth=model_params.max_depth,  # 30
        bootstrap=model_params.bootstrap,  # True
        target_column=target_column_name
    )

     return model_trainer_config


