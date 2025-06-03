from src.health_insurance import logger
from src.health_insurance.components.datatransformation import Datatransformation
from src.health_insurance.config.configuration import ConfigurationManager

STAGE_NAME="Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config_details=ConfigurationManager()
        get_config_deatils=config_details.get_data_transformation_config()
        data_transformatio=Datatransformation(config=get_config_deatils)
        data_transformatio.transfornming_data()