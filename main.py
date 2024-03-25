from mobilePriceRangePrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mobilePriceRangePrediction.logging import logger

try:
    logger.info("Data ingestion stage started.")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("Data ingestion stage completed.")
except Exception as e:
    logger.exception(e)
    raise e
