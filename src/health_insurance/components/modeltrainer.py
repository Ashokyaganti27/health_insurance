from src.health_insurance import logger
from src.health_insurance.entity.config_entity import ModelTrainerConfig
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import os
from src.health_insurance.utils.common import save_model
class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config=config
    
    def model_training(self):
        config=self.config

        data=pd.read_csv(config.train_path)
        
        x=data.drop("Response",axis=1)

        y=data["Response"]

        model=DecisionTreeClassifier(max_depth=config.max_depth,min_samples_leaf=config.min_samples_leaf,
                                     min_samples_split=config.min_samples_split)
        
        model.fit(x,y)

        logger.info(f"Model Trained successfully ")
        
        
        model_path=os.path.join(config.root_dir,config.model_name)

        save_model(model,model_path)

        logger.info(f"Model saved at {config.root_dir}")


