from text_summarization.logging import logger
from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.data_transformation import DataTransformation



class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            logger.error(f"Error in data transformation pipeline: {e}")
            raise e
if __name__ == "__main__":
    pipeline = DataTransformationTrainingPipeline()
    pipeline.main()