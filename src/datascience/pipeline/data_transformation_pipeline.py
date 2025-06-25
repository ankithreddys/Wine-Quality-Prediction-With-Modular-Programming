from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from pathlib import Path

class DataTransformationPipeline:
    def __init__(self):
        pass
    def inititate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
            if bool(status)==True:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.data_split()
            
            else:
                raise Exception("Data Scheme is Not Valid")
        
        except Exception as e:
            print(e)