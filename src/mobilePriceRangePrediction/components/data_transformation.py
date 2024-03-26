import os
from typing import List
from mobilePriceRangePrediction.utils.common import save_object
from mobilePriceRangePrediction.entity import DataTransformationConfig

import numpy as np
import pandas as pd
from mobilePriceRangePrediction.logging import logger
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_data(self):
        ### Check validation status
        with open(self.config.validation_status, 'r') as file:
            validation_status = file.read().strip()
            if not validation_status:
                logger.info('Dataset failed at validation.')
                return 
        ### Read raw data
        raw_data = self.config.raw_data_path+'/train.csv'
        df = pd.read_csv(raw_data)

        ### Split the data
        train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

        ### Preprocess the data
        # Clean Data
        train_df = self.get_clean_data(train_df)
        test_df = self.get_clean_data(test_df)

        # Transform data
        target_feature = 'price_range'
        num_features = train_df.drop(target_feature, axis=1).select_dtypes(include='number').columns
        cat_features = train_df.select_dtypes(include='object').columns 
        
        preprocessor = self.get_data_tranformer_object(num_features,cat_features)
        
        input_feature_train_df = train_df.drop(columns=[target_feature])
        target_feature_train_df = train_df[target_feature]

        input_feature_test_df = test_df.drop(columns=[target_feature])
        target_feature_test_df = test_df[target_feature]
        
        input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
        target_feature_train_arr = np.array(target_feature_train_df)

        inpute_feature_test_arr = preprocessor.transform(input_feature_test_df)
        target_feature_test_arr = np.array(target_feature_test_df)

        train_arr = np.c_[input_feature_train_arr, target_feature_train_arr]
        test_arr = np.c_[inpute_feature_test_arr, target_feature_test_arr]

        ### Save the preprocessor
        save_object(
            file_path = os.path.join(self.config.preprocessor_path,'preprocessor.pkl'),
            obj = preprocessor
        )
        
        ### Save the data
        save_object(
            file_path = os.path.join(self.config.local_data_file,'train_arr.pkl'),
            obj = train_arr
        )

        save_object(
            file_path = os.path.join(self.config.local_data_file,'test_arr.pkl'),
            obj = test_arr
        )

    def get_clean_data(self, data):
        """
        This function returns the cleaned data
        """
        replace_map = {0: 'No', 1: 'Yes'}
        features_to_replace = ['blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi']
        data[features_to_replace] = data[features_to_replace].replace(replace_map)
        return data
    
    def get_data_tranformer_object(self, num_features, cat_features):
        """
        This function is responsible for creating a preprocessor object
        """
        num_pipeline = Pipeline(
            steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ]
        )

        cat_pipeline = Pipeline(
            steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('ohe', OneHotEncoder(handle_unknown='ignore', drop='first'))
            ]
        )

        preprocessor = ColumnTransformer(
            transformers=[
                ('num_pipeline', num_pipeline, num_features),
                ('cat_pipeline', cat_pipeline, cat_features)
            ],
            remainder='drop'
        )

        return preprocessor  
     