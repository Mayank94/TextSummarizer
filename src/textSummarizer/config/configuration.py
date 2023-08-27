from textSummarizer.constants import *  # we have defined some contant paths in constants
from textSummarizer.utils.common import read_yaml, create_directories # done in utils' common.py file
from textSummarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath) # since read yaml returns config box we can access dict as we do object method ie with a do dict.key = value
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(    #
            root_dir=config.root_dir,   # directly reading from config.yaml file and if we want to change something we will do it there and not here
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config