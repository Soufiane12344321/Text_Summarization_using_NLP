from text_summarization.logging import logger
from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.data_ingestion import DataIngestion

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            logger.error(f"Error in data ingestion pipeline: {e}")
            raise e

if __name__ == "__main__":
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
