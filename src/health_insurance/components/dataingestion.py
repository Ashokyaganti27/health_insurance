import os
from src.health_insurance.entity.config_entity import DataIngestonConfig
from kaggle.api.kaggle_api_extended import KaggleApi
from src.health_insurance import logger
import zipfile
from pathlib import Path
class DataIngestion:
    def __init__(self,config:DataIngestonConfig):

        self.config=config

    def downloading_data_from_kaggle(self):
        config=self.config
        logger.info("Downloading Datset from kaggle")

        os.environ["KAGGLE_CONFIG_DIR"] = os.path.join(os.getcwd(), ".kaggle")

        if Path(config.file_path_zip).exists():
            logger.info(f"datset already downloaded at {config.file_path_zip}, skipping downloading")
            return 

        api=KaggleApi()
        api.authenticate()

        api.dataset_download_files(
            dataset=config.dataset_name,
            path=config.root_dir,
            unzip=False
        )

        # renaming downloded zip file into custom
        
        logger.info(f"Dataset successfully Downloaded at {config.root_dir}")

        downloaded_zip_path=Path(config.root_dir) / f"{config.dataset_name.split('/')[-1]}.zip"
        target_zip_path=Path(config.file_path_zip)

        if downloaded_zip_path.exists():
            os.rename(downloaded_zip_path,target_zip_path)


        logger.info(f"Dataset successfully renamed")


    def extract_data(self):

        logger.info("Extracting Downloded data")

        with zipfile.ZipFile(self.config.file_path_zip,"r") as zip_ref:
            zip_ref.extractall(self.config.root_dir)

        logger.info(f"Extracted Zip file to {self.config.root_dir}")
        
