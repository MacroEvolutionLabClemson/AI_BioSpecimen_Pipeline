ARTIFACTS_DIR: str = "artifacts"   #A string constant specifying the base directory ("artifacts") where all generated files and outputs (artifacts) of the training pipeline will be stored.

'''
Here, we mention the 'constant variables' related or used in the data_ingestion component and also throughout the project
'''

DATA_INGESTION_DIR_NAME: str = "data_ingestion"         #A string constant that names the subdirectory ("data_ingestion") where the data ingestion component's output will be stored.

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"     #A string constant that specifies the subdirectory ("feature_store") inside the data ingestion sub-directory where the  dataset files will be unzipped and stored.

DATA_DOWNLOAD_URL: str = "ENTER RAW DATASET URL"



'''
Here, we mention the 'constant variables' related or used in the data_validation component and also throughout the project
'''

DATA_VALIDATION_DIR_NAME: str = "data_validation"         #A string constant that names the subdirectory ("data_validation") where the data validation component's output will be stored.

DATA_VALIDATION_STATUS_FILE = 'status.txt'                 #A string constant that is the name of a txt file that stores the output (True or False) of the data_validation component

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "test", "data.yaml"]        #These are the list of files that need to be present in our unzipped dataset. If these are present, data_validation component returns a True, and we can move ahead with model training.

'''
Here, we mention the 'constant variables' related or used in the model_trainer component and also throughout the project
'''

MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov8s-seg.pt"

MODEL_TRAINER_NO_EPOCHS: int = 50