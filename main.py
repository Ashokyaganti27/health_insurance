from src.health_insurance import logger
from src.health_insurance.pipeline.data_ingestion_pipeline import DataIngetionTrainingPipeline
from src.health_insurance.pipeline.data_validation_pipeline import DataValidationpipeline
from src.health_insurance.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.health_insurance.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.health_insurance.pipeline.model_evaluation_pipeline import ModelevaluationPipeline

STAGE_NAME="Data Ingetion Stage"


if __name__=="__main__":
    try:
        logger.info(f"stage {STAGE_NAME} started ")
        obj=DataIngetionTrainingPipeline()
        obj.intiate_data_ingetion()
    
    except Exception as e:
        logger.info(e)
        raise e

STAGE_NAME="Data validation"
if __name__=="__main__":
    try:
        logger.info(f" Satge {STAGE_NAME} Started--")
        obj=DataValidationpipeline()
        obj.initiate_data_validation_pipeline()
    except Exception as e:
        logger.info(e)
        raise e 


STAGE_NAME="Data Transformation"

if __name__=="__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} Started ....")
        obj=DataTransformationPipeline()
        obj.initiate_data_transformation()
    except Exception as e:
        raise e



STAGE_NAME="Model Trainer"

if __name__=="__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} Started ....")
        obj=ModelTrainerPipeline()
        obj.initiate_model_training()
    except Exception as e:
        raise e


STAGE_NAME="Model Evaluation"
if __name__=="__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} Started ....")
        obj=ModelevaluationPipeline()
        obj.initiate_model_evaluation()
    except Exception as e:
        raise e





