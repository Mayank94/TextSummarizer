from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        #data_ingestion.download_file()  # if error regarding zipfile comes, simply comment it out and download the data manually in artifects folder
        
        # during our testing it was causing an issue, thus we are going to manually download and put the data in artifacts folder with name data.zip 
        data_ingestion.extract_zip_file()