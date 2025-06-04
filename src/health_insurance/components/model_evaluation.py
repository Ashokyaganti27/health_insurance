import mlflow.sklearn
import mlflow.sklearn
import pandas as pd
import os
from src.health_insurance.entity.config_entity import ModelEvaluationConfig
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from src.health_insurance.utils.common import load_model
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
import seaborn as sns
import matplotlib.pyplot as plt
from src.health_insurance import logger

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/YagantiAshok177/health_insurance.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="YagantiAshok177"
os.environ["MLFLOW_TRACKING_PASSWORD"]="956d2471d3300f480dff6a3490c4f9461bb086a8"


class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config
    
    def evaluation_metrics(self,actual,pred):
        
        # evaluating matrics

        accuracy=accuracy_score(actual,pred)

        cm=confusion_matrix(actual,pred)

        report=classification_report(actual,pred,output_dict=True)

        return accuracy,cm,report
    
    def log_mlflow(self):
        config=self.config

        data=pd.read_csv(config.test_data_path)

        model=load_model(config.model_path)

        test=data.drop(config.target_columns,axis=1)

        y_true=data[config.target_columns]

        logger.info("Model Predicting Started")

        pred_values=model.predict(test)

        accuracy,cm,report=self.evaluation_metrics(y_true,pred_values)

        mlflow.set_tracking_uri(config.mlflow_uri)

        mlflow.set_experiment("Health_Insurance_Cross_sell")

        mlflow.set_registry_uri(config.mlflow_uri)
        
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            mlflow.log_params(config.params)

            mlflow.log_metric("accuracy",accuracy)
            mlflow.log_metric("precision_class_1",report["1"]["precision"])
            mlflow.log_metric("recall",report["1"]["recall"])
            mlflow.log_metric("f1_score",report["1"]["f1-score"])

            logger.info("Successfully logged Metrics into mlflow")

            # logging confusion matrix as a plot

            plt.figure(figsize=(6,4))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=[0,1], yticklabels=[0,1])
            plt.xlabel("Predicted")
            plt.ylabel("Actual")
            plt.title("Confusion Matrix")

            plt.savefig("confusion_matrix.png")
            mlflow.log_artifact("confusion_matrix.png")

            logger.info("looges confusion matrix as png")

            # logging  classification report as File

            report =pd.DataFrame(report)
            report.to_csv("report.csv")
            mlflow.log_artifact("report.csv")

            logger.info("looged classification report")


            # logging model
        signature=infer_signature(test,y_true)
        input_example=test.head(5)
        
        if tracking_url_type_store!="file":
            mlflow.sklearn.log_model(model,"model",registered_model_name="Decision_Tree_Model",signature=signature,input_example=input_example)
        else:
            mlflow.sklearn.log_model(model,"model")
                
        os.remove("confusion_matrix.png")
        os.remove("report.csv")

  
