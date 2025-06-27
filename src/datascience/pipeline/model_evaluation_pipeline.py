from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_into_mlfow()