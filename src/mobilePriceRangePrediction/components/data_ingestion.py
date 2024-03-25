import os
from pathlib import Path
from mobilePriceRangePrediction.entity import DataIngestionConfig
from mobilePriceRangePrediction.constants import *
from mobilePriceRangePrediction.logging import logger
from mobilePriceRangePrediction.utils.common import get_size
from kaggle.api.kaggle_api_extended import KaggleApi

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            # Initialize Kaggle API client
            api = KaggleApi()

            # Authenticate with your Kaggle API credentials
            api.authenticate()  # This will use your Kaggle API token stored in ~/.kaggle/kaggle.json

            # Download the dataset
            api.dataset_download_files(
                dataset=self.config.source, 
                path=self.config.local_data_file, 
                unzip=True
            )

            logger.info("Dataset downloaded successfully.")
            print("Dataset downloaded successfully.")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  
            