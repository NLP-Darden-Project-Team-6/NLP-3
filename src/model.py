import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing import tfidf_scaler, train_validate_test_split, scale_numeric_columns

def model_data():
    '''
    
    '''
    
    df = pd.read_csv('../../data/model/model_readme_data.csv')
    
    X = df.drop(columns='language_y')
    y = df.language_y
    
    X_train, y_train, X_validate, y_validate, X_test, y_test = train_validate_test_split(X, y)
    X_train, X_validate, X_test = scale_numeric_columns(X_train, X_validate, X_test)
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test