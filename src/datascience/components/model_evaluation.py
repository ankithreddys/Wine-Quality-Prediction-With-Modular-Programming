from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience import logger
from src.datascience.utils.common import load_json, save_json, load_bindata
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2
    
    def log_into_mlfow(self):
        X_test = pd.read_csv(self.config.test_X_path)
        y_test = pd.read_csv(self.config.test_y_path)

        model = load_bindata(Path(self.config.model_path))
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            pred = model.predict(X_test)

            (rmse, mae, r2) = self.eval_metrics(y_test, pred)
            metrics = {"rmse" : rmse, "mae" : mae, "r2" : r2}
            save_json(Path(self.config.model_metrics),metrics)

            mlflow.log_params(load_json(Path(self.config.best_params_path)))

            mlflow.log_metrics(metrics)

            mlflow.log_artifact(str(self.config.model_path), "model")
            logger.info("Model logged successfully as artifact")
