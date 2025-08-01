'''
In this module, we actually train the model. To train the model, we use bash scripting commands
'''

import os, sys
import yaml
from segmentation.utils.main_utils import read_yaml_file
from segmentation.logger import logging
from segmentation.exception import AppException
from segmentation.entity.config_entity import ModelTrainerConfig
from segmentation.entity.artifacts_entity import ModelTrainerArtifact



class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def correct_yaml_paths(self):
        """Correct the paths in data.yaml file"""
        try:
            with open("data.yaml", "r") as f:
                data_config = yaml.safe_load(f)

            current_dir = os.getcwd()

            # Update paths to use ./ instead of ../
            data_config['train'] = os.path.join(current_dir, 'train', 'images')
            data_config['val'] = os.path.join(current_dir, 'valid', 'images')
            data_config['test'] = os.path.join(current_dir, 'test', 'images')

            # Replace backslashes with forward slashes for YOLO compatibility -- If this code is ever run on Windows, this portion gets executed
            data_config['train'] = data_config['train'].replace('\\', '/')
            data_config['val'] = data_config['val'].replace('\\', '/')
            data_config['test'] = data_config['test'].replace('\\', '/')

            logging.info(f"Updated train path: {data_config['train']}")
            logging.info(f"Updated val path: {data_config['val']}")
            logging.info(f"Updated test path: {data_config['test']}")

            with open("data.yaml", "w") as f:
                yaml.dump(data_config, f)

            logging.info("Successfully corrected paths in data.yaml")


        except Exception as e:
            raise AppException(e, sys)
        

    def initiate_model_trainer(self)-> ModelTrainerArtifact:
        logging.info("Entered the initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            # Ensure we're in the correct directory
            original_dir = os.getcwd()


            os.system("unzip data.zip")     #os.system() executes the commands in the underlying terminal
            os.system("rm data.zip")        #delete data.zip after it is unzipped

            # Correct yaml paths before training
            self.correct_yaml_paths()

            os.system(f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} data={os.path.join(original_dir, 'data.yaml')} epochs={self.model_trainer_config.no_epochs} imgsz=640 batch=16 save=true")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok = True)
            
            os.system(f"cp runs/segment/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")

            os.system("rm -rf yolov8s-seg.pt")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
            os.system("rm -rf runs")
            os.system("rm -rf README.dataset.txt")
            os.system("rm -rf README.roboflow.txt")

            

            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path = "artifacts/model_trainer/best.pt")

            logging.info("Exited the initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model Trainer Artifact: {model_trainer_artifact}")

            return model_trainer_artifact
        
        except Exception as e:
            raise AppException(e,sys)