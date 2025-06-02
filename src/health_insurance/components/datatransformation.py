from src.health_insurance import logger
import pandas as pd

from src.health_insurance.entity.config_entity import DataTransformationConfig

class DatatransformationConfig:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
    
    def transfornming_data(self):

        train=pd.read_csv(self.config.train)
        test=pd.read_csv(self.config.test)

        # here both has id columns that not important 

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

        vechile_age={
            "1-2 Year":1,
            "> 2 Years":2,
            "< 1 Year":0
        }

        train["Vehicle_Damage"]=train["Vehicle_Age"].map(vechile_age)
        test["Vehicle_Damage"]=test["Vehicle_Age"].map(vechile_age)

        

                

