import os
from mobilePriceRangePrediction.entity import DataValidationConfig
from mobilePriceRangePrediction.logging import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(os.path.join('artifacts','data','raw'))

            for file in self.config.ALL_REQUIRED_FILES:
                validation_status = False if file not in all_files else True
                
                with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation status: {validation_status}')
                
                if validation_status == False:
                     break
            
            logger.info("All required files exist.")
            return validation_status
        except Exception as e:
             logger.info("Failed to find all required files.")
             raise e
        