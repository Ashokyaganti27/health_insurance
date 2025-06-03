from src.health_insurance import logger
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.health_insurance.entity.config_entity import DataTransformationConfig
import os

class Datatransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
    
    def transfornming_data(self):
        
        train=pd.read_csv(self.config.train)
        test=pd.read_csv(self.config.test)

        # here both has id columns that not important 
        logger.info("data transformation Started--")
        train.drop("id",axis=1,inplace=True)
        test.drop("id",axis=1,inplace=True)

        # we have three categorical variable vechile_damage,gender,vechile_age 

        # Gender has two uniue values so we can convert into 0,1

        train["Gender"]=train["Gender"].map({"Male":1,"Female":0})
        test["Gender"]=test["Gender"].map({"Male":1,"Female":0})

        # now vechile damage has also two unque values

        train["Vehicle_Damage"]=train["Vehicle_Damage"].map({"Yes":1,"No":0})
        test["Vehicle_Damage"]=test["Vehicle_Damage"].map({"Yes":1,"No":0})

        # now vechile age , actually i claimed an assumption if car age is less that person take insurance 
        # so i decided  to test my assumption it failed surprisely it got older car owners are buying insurance heavily when compared to less 
        # i understanded that if car is young it has some warranty and also dealarships provide 1 to 2 years insurance 
        # Vehicle_Age
        # 1-2 Year     0.173755 
        # < 1 Year     0.043705
        # > 2 Years    0.293746

        Vehicle_Age={
            "1-2 Year":1,
            "> 2 Years":2,
            "< 1 Year":0
        }

        train["Vehicle_Age"]=train["Vehicle_Age"].map(Vehicle_Age)
        test["Vehicle_Age"]=test["Vehicle_Age"].map(Vehicle_Age)
        
        logger.info(f"categorical columns are encoded")

        # scaling only for distance based models not tress based models
        # so if self.config is trus we transform otherwise not 

        if self.config:
            scaling_features=["Age","Region_Code","Annual_Premium","Policy_Sales_Channel","Vintage"]

            scaler=StandardScaler()

            scaler.fit(train[scaling_features])

            # transforming

            train_scaled=scaler.transform(train[scaling_features])
            test_scaled=scaler.transform(test[scaling_features])

            # 2. Convert to DataFrames with same column names
            train_scaled_df = pd.DataFrame(train_scaled, columns=scaling_features)
            test_scaled_df = pd.DataFrame(test_scaled, columns=scaling_features)


            train_scaled=pd.concat([train_scaled_df,train.drop(scaling_features,axis=1).reset_index(drop=True)],axis=1)
            test_scaled=pd.concat([test_scaled_df,test.drop(scaling_features,axis=1).reset_index(drop=True)],axis=1)

            
            train_path=os.path.join(self.config.root_dir,"train.csv")
            test_path=os.path.join(self.config.root_dir,"test.csv")


            # saving processed data

            train_scaled.to_csv(train_path,index=False)
            test_scaled.to_csv(test_path,index=False)

            logger.info(f"Data Transformation completed and saved into {self.config.root_dir}")
    
        else:
                
            train_path=os.path.join(self.config.root_dir,"train.csv")
            test_path=os.path.join(self.config.root_dir,"test.csv")


            train.to_csv(train_path,index=False)
            test.to_csv(test_path,index=False)

            logger.info(f"Data Transformed successfully saved into {self.config.root_dir}")
            
 
                

