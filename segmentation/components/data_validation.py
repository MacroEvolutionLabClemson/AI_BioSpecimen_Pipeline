'''
This component checks that the folders created after the data ingestion process is in the right 
format or not. Basically, it'll check artifacts/data_ingestion/feature_store has all test, train,
valid, data.yaml file and folders.
'''

import os, sys
import shutil
from segmentation.exception import AppException
from segmentation.logger import logging
from segmentation.entity.config_entity import DataValidationConfig
from segmentation.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact



class DataValidation:
    def __init__(self, 
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise AppException(e,sys)
        
    
    def validate_all_file_exist(self) -> bool:
        try:
            feature_store_files = os.listdir(self.data_ingestion_artifact.feature_store_path)

            validation_status = True
            for required_file in self.data_validation_config.required_file_list:
                if required_file not in feature_store_files:
                    validation_status = False
                    break  # No need to continue checking if even one file is missing

            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            with open(self.data_validation_config.valid_status_file_dir, "w") as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            raise AppException(e, sys)
        
    def initiate_data_validation(self)-> DataValidationArtifact:
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_file_exist()
            data_validation_artifact = DataValidationArtifact(validation_status = status)

            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data Validation Artifact: {data_validation_artifact}")

            if status:              #Here, we are just copying the data.zip file from artifacts folder to the root directory
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())
                
            return data_validation_artifact
        except Exception as e:
            raise AppException(e,sys)

        