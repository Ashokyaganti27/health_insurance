from src.health_insurance import logger
from src.health_insurance.pipeline.data_ingestion_pipeline import DataIngetionTrainingPipeline
from src.health_insurance.pipeline.data_validation_pipeline import DataValidationpipeline
# STAGE_NAME="Data Ingetion Stage"


# if __name__=="__main__":
#     try:
#         logger.info(f"stage {STAGE_NAME} started ")
#         obj=DataIngetionTrainingPipeline()
#         obj.intiate_data_ingetion()
    
#     except Exception as e:
#         logger.info(e)
#         raise e

STAGE_NAME="Data validation"
if __name__=="__main__":
    try:
        logger.info(f" Satge {STAGE_NAME} Started--")
        obj=DataValidationpipeline()
        obj.initiate_data_validation_pipeline()
    except Exception as e:
        logger.info(e)
        raise e 
