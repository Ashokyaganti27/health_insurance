from src.health_insurance import logger
from src.health_insurance.config.configuration import ConfigurationManager
from src.health_insurance.components.modeltrainer import ModelTrainer

STAGE_NAME="MODEL TRAINER"

class ModelTrainerPipeline:

    def __init__(self):
        pass
        
    def initiate_model_training(self):
        config_deatils=ConfigurationManager()
        get_config_details=config_deatils.get_model_trainer_config()
        model_trainer=ModelTrainer(config=get_config_details)
        model_trainer.model_training()