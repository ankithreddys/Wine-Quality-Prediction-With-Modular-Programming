from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    data_file_csv: Path
    STATUS_FILE: str
    all_schema: dict


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_file_csv: Path
    schema: dict


@dataclass
class ModelTrainingConfig:
    root_dir: Path
    train_df_path: Path
    test_df_path: Path
    model_name: str
    best_params_path: Path
    n_estimators: list
    learning_rate: list
    max_depth: list
    random_state: int
    n_splits: int
    shuffle: bool
    scoring: str
    n_jobs: int
    verbose: int
    schema: dict


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_X_path: Path
    test_y_path: Path
    model_path: Path
    model_metrics: Path
    best_params_path: Path
    mlflow_uri: str
    schema: dict
    

