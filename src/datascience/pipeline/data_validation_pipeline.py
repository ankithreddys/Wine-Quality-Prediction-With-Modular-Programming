from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation


class DataValidationPieline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()
        