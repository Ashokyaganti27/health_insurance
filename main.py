from src.health_insurance import logger
from src.health_insurance.pipeline.data_ingestion_pipeline import DataIngetionTrainingPipeline

STAGE_NAME="Data Ingetion Stage"


if __name__=="__main__":
    try:
        logger.info(f"stage {STAGE_NAME} started ")
        obj=DataIngetionTrainingPipeline()
        obj.intiate_data_ingetion()
    
    except Exception as e:
        logger.info(e)
        raise e
