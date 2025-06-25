from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass
    def inititate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.data_split()
