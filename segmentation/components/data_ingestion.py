'''
This is the actual data ingestion component. That is, this is where the actual data ingestion logic lives. The data ingestion 
component downloads and extracts a dataset from Roboflow's raw link and prepares it for downstream pipeline components.
'''
import os
import sys
import zipfile
import requests
from segmentation.exception import AppException
from segmentation.logger import logging
from segmentation.entity.config_entity import DataIngestionConfig
from segmentation.entity.artifacts_entity import DataIngestionArtifact

class DataIngestion:
    #This DataIngestion class (component) will be instantiated in your pipeline.
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppException(e, sys)

    def download_data(self) -> str:
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)

            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)

            logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")
            response = requests.get(dataset_url)
            with open(zip_file_path, "wb") as f:
                f.write(response.content)
            logging.info("Download complete.")
            return zip_file_path

        except Exception as e:
            raise AppException(e, sys)
    
    def extract_zip_file(self, zip_file_path: str) -> str:
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)
            logging.info(f"Extracted zip file: {zip_file_path} into dir: {feature_store_path}")
            return feature_store_path
        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )

            logging.info("Exiting initiate_data_ingestion method of DataIngestion class")
            logging.info(f"Data Ingestion artifacts: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)