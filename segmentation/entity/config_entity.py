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
