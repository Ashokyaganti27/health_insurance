from src.health_insurance import logger
from src.health_insurance.config.configuration import ConfigurationManager
from src.health_insurance.components.model_evaluation import ModelEvaluation

STAGE_NAME="Model Evaluation "

class ModelevaluationPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        config_details=ConfigurationManager()
        get_config=config_details.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=get_config)
        model_evaluation.log_mlflow()
    
