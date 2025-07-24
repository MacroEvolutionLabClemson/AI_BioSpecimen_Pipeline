'''
This file defines artifact entities, i.e., this file is used to represent or define the outputs (or results) of each 
pipeline component.
'''

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    #This class represents the output of the data ingestion component. It stores:
    # The path where the downloaded zip file is saved (data.zip)
    # The path to the folder where the unzipped dataset is stored (feature_store)

    data_zip_file_path: str
    feature_store_path: str

@dataclass
class DataValidationArtifact:
    #Output of the data validation process: 1. A boolean value inside status.txt. When it is true, it
    #means the artifacts/data_ingestion/feature_store has all the files required for training purpose
    
    validation_status:bool
