''' 
A config entitiy refers to a structured data object (usually a class) that holds configuration information for each component
 — such as directory paths, URLs, file names, constants, or hyperparameters — that the pipeline components need to function 
 properly.
'''
import os
from dataclasses import dataclass
from segmentation.constant.training_pipeline import *

@dataclass
class TrainingPipelineConfig:
    #This class defines where all pipeline outputs (artifacts) should be stored.

    artifacts_dir: str = ARTIFACTS_DIR

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    #This defines the folder where all outputs related to data ingestion will go. (data_ingestion)
    #It also defines the subfolder where unzipped raw dataset will be saved. (feature_store)
    #It also holds the URL to download your dataset from

    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME)

    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)

    data_download_url: str = DATA_DOWNLOAD_URL

@dataclass
class DataValidationConfig:                     
    #The input that is given to the data validation component:
    #  1. path where the data_validation sub directory needs to be created inside artifacts directory.
    #  2) path inside this subdirectory where status.txt is saved which says whether the format of the data is correct or not.
    #  3) list of files that needs to be present in artifacts/data_ingestion/feature_store so that status.txt says 'valid'
    
    data_validation_dir: str = os.path.join(training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME)   #artifacts/data_validation

    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)     #artifacts/data_validation/status.txt

    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES   
