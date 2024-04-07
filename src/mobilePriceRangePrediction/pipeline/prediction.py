from mobilePriceRangePrediction.config.configuration import ConfigurationManager
from mobilePriceRangePrediction.utils.common import load_object

class PredictionPipeline:
    def __init__(self):
        # Access model
        self.config = ConfigurationManager().get_prediction_config()

    def predict(self, data):
        # Get the preprocessor
        preprocessor = load_object(self.config.preprocessor_path)
        
        # Get the model
        model = load_object(self.config.model_path)

        # Transform the data
        transformed_data = preprocessor.transform(data)
        
        # Make the prediction
        prediction = model.predict(transformed_data)
        
        return prediction
    