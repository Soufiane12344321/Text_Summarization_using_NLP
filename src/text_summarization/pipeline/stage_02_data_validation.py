from text_summarization.logging import logger
from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.data_validation import DataValiadtion


class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            logger.error(f"Error in data validation pipeline: {e}")
            raise e
if __name__ == "__main__":
    pipeline = DataValidationTrainingPipeline()
    pipeline.main()