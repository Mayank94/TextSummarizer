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