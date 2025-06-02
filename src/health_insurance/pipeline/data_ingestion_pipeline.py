from src.health_insurance import logger
from src.health_insurance.config.configuration import ConfigurationManager
from src.health_insurance.components.dataingestion import DataIngestion

class DataIngetionTrainingPipeline:
    def __ini__(self):
        pass

    def intiate_data_ingetion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.downloading_data_from_kaggle()
        data_ingestion.extract_data()
    
