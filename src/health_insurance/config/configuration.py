import os 
from src.health_insurance.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from src.health_insurance.utils.common import read_yaml,create_directories
from src.health_insurance.entity.config_entity import DataIngestonConfig
from src.health_insurance.entity.config_entity import DataValidationConfig
from src.health_insurance.entity.config_entity import DataTransformationConfig
from src.health_insurance.entity.config_entity import ModelTrainerConfig
from src.health_insurance.entity.config_entity import ModelEvaluationConfig
class ConfigurationManager:
    def __init__(self,config_fil=CONFIG_FILE_PATH,
                 params_file=PARAMS_FILE_PATH,
                 schema_file=SCHEMA_FILE_PATH):
        
        self.config=read_yaml(config_fil)
        self.params=read_yaml(params_file)
        self.schema_file=read_yaml(schema_file)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) ->DataIngestonConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestonConfig(

            root_dir=config.root_dir,
            dataset_name=config.dataset_name,
            file_path_zip=config.file_path_zip
        )

        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema_file
        create_directories([config.root_dir])

        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema.columns,
            test_data_path=config.test_data_path
        )

        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation

        create_directories([config.root_dir])

        data_transfomation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            train=config.train,
            test=config.test,
            scaling=config.scaling
        )
        
        return data_transfomation_config
    
    def get_model_trainer_config(self)->ModelTrainerConfig:

        config=self.config.model_trainer
        params=self.params.Decision_tree
        
        create_directories([config.root_dir])

        model_trainer_config=ModelTrainerConfig(
            root_dir=config.root_dir,
            train_path=config.train_path,
            model_name=config.model_name,
            max_depth=params.max_depth,
            min_samples_leaf=params.min_samples_leaf,
            min_samples_split=params.min_samples_split
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self)->ModelEvaluationConfig:

        config=self.config.model_evaluation
        schema=self.schema_file.target_column
        params=self.params.Decision_tree

        create_directories([config.root_dir])

        data_model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_file_name=config.metrics_file_name,
            model_path=config.model_path,
            target_columns=schema.target,
            mlflow_uri="https://dagshub.com/YagantiAshok177/health_insurance.mlflow",
            params=params

        )
        return data_model_evaluation_config