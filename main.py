from mobilePriceRangePrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mobilePriceRangePrediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mobilePriceRangePrediction.logging import logger

# Data Ingestion
try:
    logger.info("Data ingestion stage started.")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("Data ingestion stage completed.")
except Exception as e:
    logger.exception(e)
    raise e

# Data Validation
try:
    logger.info("Data validation stage started.")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info("Data validation stage completed.")
except Exception as e:
    logger.exception(e)
    raise e
