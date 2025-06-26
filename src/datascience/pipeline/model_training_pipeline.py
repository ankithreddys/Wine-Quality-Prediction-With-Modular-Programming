from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_training import ModelTraining



class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config = ConfigurationManager()
        model_training_config = config.get_training_config()
        model_training = ModelTraining(model_training_config)
        model_training.cross_validation()