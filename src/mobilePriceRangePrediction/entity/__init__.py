from dataclasses import dataclass
from pathlib import Path
from pydantic import BaseModel

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source: str
    local_data_file: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    raw_data_path: Path
    validation_status: str
    local_data_file: Path
    preprocessor_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path 

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    metric_file_name: Path

@dataclass(frozen=True)
class ModelPredictionConfig:
    root_dir: Path
    preprocessor_path: Path
    model_path: Path

class PredictionRequest(BaseModel):
    battery_power: int
    blue: str
    clock_speed: float
    dual_sim: str
    fc: int
    four_g: str
    int_memory: int
    m_dep: float
    mobile_wt: int
    n_cores: int
    pc: int
    px_height: int
    px_width: int
    ram: int
    sc_h: int
    sc_w: int
    talk_time: int
    three_g: str
    touch_screen: str
    wifi: str
