import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing import tfidf_scaler, train_validate_test_split, scale_numeric_columns


def model_data(path_name=''):
    '''
    
    '''
    df = pd.read_csv(f'{path_name}/model_readme_data.csv')
    
    X = df.drop(columns='language_y')
    y = df.language_y
    
    X_train, y_train, X_validate, y_validate, X_test, y_test = train_validate_test_split(X, y)
    X_train, X_validate, X_test = scale_numeric_columns(X_train, X_validate, X_test)
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test


def model_scores(model_1_acc=np.nan, model_2_acc=np.nan, model_3_acc=np.nan, modeling_set=''):
    '''
    
    '''
    
    model_scores = pd.DataFrame({'ridge': model_1_acc,
                                 'random_forest': model_2_acc,
                                 'gradient_boost': model_3_acc},
                                index=[modeling_set])
    
    return model_scores


def model_evals(train_scores, validate_scores, test_scores):
    '''
    
    '''
    df = pd.concat([train_scores, validate_scores, test_scores])
    return df