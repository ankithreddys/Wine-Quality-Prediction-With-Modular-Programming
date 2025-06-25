from src.datascience.entity.config_entity import DataValidationConfig
from src.datascience import logger
import pandas as pd


class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self):
        try:
            validation_status = None

            df = pd.read_csv(self.config.data_file_csv, delimiter=";")
            cols = list(df.columns)

            all_schema = self.config.all_schema.keys()

            for col in cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "a") as f:
                        f.write(f"Validation status: {validation_status}\n")
                    logger.info(f"Validation of Data Schema Failed for {col}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "a") as f:
                        f.write(f"Validation status: {validation_status}\n")
                    logger.info(f"Validation of Data Schema Passed for {col}")
            
            return validation_status
        
        except Exception as e:
            raise e
            
