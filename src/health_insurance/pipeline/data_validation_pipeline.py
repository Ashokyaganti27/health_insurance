from src.health_insurance.config.configuration import ConfigurationManager
from src.health_insurance.components.datavalidation import DataValidation
from src.health_insurance import logger

STAGE_NAME="Data validation"

class DataValidationpipeline:
    def __init__(slef):
        pass


    def initiate_data_validation_pipeline(self):
        config_details=ConfigurationManager()
        data_validation_config=config_details.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.data_validation_checking()
