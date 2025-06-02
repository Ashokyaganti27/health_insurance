from src.health_insurance import logger
from src.health_insurance.entity.config_entity import DataValidationConfig
import pandas as pd
class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config=config
    
    def data_validation_checking(self):

        data=pd.read_csv(self.config.test_data_path)

        columns=list(data.columns)

        data_types=list(self.config.all_schema.values())

        schema_data=list(self.config.all_schema.keys())

        for i in range(len(schema_data)):
            try:
                if not (columns[i]==schema_data[i] and data[columns[i]].dtype==data_types[i]):

                    status_file=False

                    with open(self.config.STATUS_FILE,"w") as file:
                        file.write(f"{status_file}")
                        logger.info(f"Data is miss matched at column {columns[i]}")
                        return 
                else:
                    status_file=True
                    with open(self.config.STATUS_FILE,"w") as file:
                        file.write(f"{status_file}")
                        logger.info(f"Datavalidation is successfull---")

                        return 
            except Exception as e:
                raise e


