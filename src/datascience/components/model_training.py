from src.datascience.entity.config_entity import ModelTrainingConfig
from src.datascience import logger
from xgboost import XGBRegressor
from sklearn.model_selection import KFold, GridSearchCV
from src.datascience.utils.common import save_bin
import pandas as pd
import os
from pathlib import Path



class ModelTraining:
    def __init__(self, config:ModelTrainingConfig):
        self.config = config
    
    def data_loading(self):
        training_df = pd.read_csv(self.config.train_df_path)
        testing_df = pd.read_csv(self.config.test_df_path)

        X_train = training_df.drop([self.config.schema.name], axis=1)
        y_train = training_df[self.config.schema.name]
        logger.info(f"Training Dependent Variables info : {X_train.shape}")
        logger.info(f"Training InDependent Variables info : {y_train.shape}")

        X_test = testing_df.drop([self.config.schema.name], axis=1)
        y_test = testing_df[self.config.schema.name]
        logger.info(f"Testing Dependent Variables info : {X_test.shape}")
        logger.info(f"Testing InDependent Variables info : {y_test.shape}")

        X_test.to_csv(os.path.join(self.config.root_dir,"X_test.csv"), index=False)
        logger.info(f"X_test saved at : {os.path.join(self.config.root_dir,"X_test.csv")}")

        y_test.to_csv(os.path.join(self.config.root_dir,"y_test.csv"), index=False)
        logger.info(f"y_test saved at : {os.path.join(self.config.root_dir,"y_test.csv")}")

        return (X_train, X_test, y_train, y_test)
    

    def model_trainer(self):
        regressor = XGBRegressor()
        logger.info(f"Regressor Defined")

        param_grid = {
            "n_estimators" : self.config.n_estimators,
            "max_depth" : self.config.max_depth,
            "learning_rate" : self.config.learning_rate
        }
        logger.info(f"Params Set for Training are : {param_grid}")

        return (regressor, param_grid)
    
    def cross_validation(self):
        kf = KFold(n_splits=self.config.n_splits, shuffle=self.config.shuffle, random_state=self.config.random_state)

        regressor, param_grid = self.model_trainer()

        grid_cv = GridSearchCV(estimator=regressor, param_grid=param_grid,
                               cv=kf, scoring=self.config.scoring,
                               n_jobs=self.config.n_jobs, verbose=self.config.verbose)
        
        X_train,_,y_train,_ = self.data_loading()
        grid_cv.fit(X_train,y_train)

        logger.info(f"Best Params : {grid_cv.best_params_}")
        best_model = grid_cv.best_estimator_
        
        model_path = os.path.join(self.config.root_dir,self.config.model_name)
        save_bin(best_model,Path(model_path))
        logger.info(f"Model Saved at : {model_path}")
        

