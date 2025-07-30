from segmentation.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":
    obj = TrainPipeline()
    obj.run_pipeline()
    print("Ingestion, Validation and Model Training completed")