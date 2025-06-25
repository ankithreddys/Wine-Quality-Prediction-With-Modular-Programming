from src.datascience.config.configuration import DataTransformationConfig
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import os

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config

    def data_split(self):
        df = pd.read_csv(self.config.data_file_csv, delimiter=";")
        # target_column = self.config.schema.values
        # X = df.drop([target_column], axis=1)
        # y = df[target_column]

        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)

        train, test = train_test_split(df, test_size=0.3, random_state=6)

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'), index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"), index = False)

        logger.info(f"Created Training and Testing files in {self.config.root_dir}")
        logger.info(f"Shape of training df : {train.shape}")
        logger.info(f"Shape of testing df : {test.shape}")
        




