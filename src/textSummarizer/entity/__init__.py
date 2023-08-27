# we are creating "entity" ie defining of return type of variables in dataingestion config

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:      # this is not a normal class its dataclass
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# we are making our code modular so that's why we are doing it
# instead of notebook, notebook was just experimentation

# data validation entity
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


# data transform entity
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

# model trainer
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int