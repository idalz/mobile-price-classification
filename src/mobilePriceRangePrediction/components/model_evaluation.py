from mobilePriceRangePrediction.entity import ModelEvaluationConfig
from mobilePriceRangePrediction.utils.common import load_object
import pandas as pd
from sklearn.metrics import f1_score, recall_score, precision_score

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_model(self):
        # Get test data
        test_arr = load_object(self.config.data_path+'/test_arr.pkl')
        X_test, y_test = test_arr[:,:-1], test_arr[:,-1]

        # Get the model
        model = load_object(self.config.model_path+'/model.pkl')
        y_pred = model.predict(X_test)
        
        # Evaluate model
        f1 = f1_score(y_test, y_pred, average='micro')
        precision = precision_score(y_test, y_pred, average='micro')
        recall = recall_score(y_test, y_pred, average='micro')
        
        # Save as .csv
        metrics_df = pd.DataFrame({
            'micro_F1_Score': [f1],
            'micro_Precision': [precision],
            'micro_Recall': [recall]
        })
        metrics_df.to_csv(self.config.metric_file_name, index=False)
