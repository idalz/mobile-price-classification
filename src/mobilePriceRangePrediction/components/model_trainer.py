import os

from mobilePriceRangePrediction.entity import ModelTrainerConfig
from mobilePriceRangePrediction.utils.common import save_object ,load_object

from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from catboost import CatBoostClassifier

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        ### Get processed data
        train_arr = load_object(self.config.data_path+'/train_arr.pkl')
        test_arr = load_object(self.config.data_path+'/test_arr.pkl')

        X_train, y_train = train_arr[:,:-1], train_arr[:,-1]
        X_test, y_test = test_arr[:,:-1], test_arr[:,-1]
        models = {
            'Logistic Regression': LogisticRegression(),
            'Decision Trees': DecisionTreeClassifier(),
            'Random Forest': RandomForestClassifier(),
            'Gradient Boosting Machines (GBM)': GradientBoostingClassifier(),
            'Support Vector Machines (SVM)': SVC(),
            'K-Nearest Neighbors (KNN)': KNeighborsClassifier(),
            'Naive Bayes': GaussianNB(),
            'AdaBoost': AdaBoostClassifier(),
            'Extra Trees Classifier': ExtraTreesClassifier(),
            'XGBoost': XGBClassifier(),
            'CatBoost': CatBoostClassifier(verbose=False)
        }

        model_report:dict = self.evaluate_models(
            X_train=X_train, y_train=y_train, 
            X_test=X_test, y_test=y_test,
            models=models
        )

        best_model_score = max(sorted(model_report.values()))
        best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
        ]

        best_model = models[best_model_name]
        
        ### TODO Fine tuning

        save_object(
            file_path=os.path.join(self.config.root_dir,'model.pkl'),
            obj = best_model
        )

    def evaluate_models(self, X_train, y_train, X_test, y_test, models):
        report = {}
            
        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            test_model_score = f1_score(y_test, y_pred, average='micro')
            report[name] = test_model_score

        return report
