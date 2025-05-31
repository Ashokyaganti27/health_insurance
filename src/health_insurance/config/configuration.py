import os 
from src.health_insurance.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from src.health_insurance.utils.common import read_yaml,create_directories
from src.health_insurance.entity.config_entity import DataIngestonConfig
class ConfiguratonManager:
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
        
    