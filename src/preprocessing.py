import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


def tfidf_scaler(df):
    '''
    
    '''
    tfidf = TfidfVectorizer()
    X_tfidf = tfidf.fit_transform(df.words)
    X = pd.concat([df[['watchers_num', 'stars_num',
                       'forks_num', 'commits_num']],
                   pd.DataFrame(X_tfidf.todense(),
                                columns=tfidf.get_feature_names())],
                  axis=1)
    y = df.language

    return X, y


def train_validate_test_split(X, y):
    '''
    
    '''
    X_train_validate, X_test, y_train_validate, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=1)
    X_train, X_validate, y_train, y_validate = train_test_split(X_train_validate, y_train_validate, stratify=y_train_validate, test_size=0.25, random_state=1)
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test


def scale_numeric_columns(X_train, X_validate, X_test):
    '''
    
    '''
    scaler = MinMaxScaler()

    # Concatenate scaled test data onto sparse matrix
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train[['watchers_num', 'stars_num',
                                                                'forks_num', 'commits_num']]))
    X_train_scaled.rename(columns={0: 'watchers_num',
                                   1: 'stars_num',
                                   2: 'forks_num',
                                   3: 'commits_num'},
                         inplace=True)

    X_train_scaled.index = X_train.index
    X_train.drop(columns=['watchers_num', 'stars_num', 'forks_num', 'commits_num'], inplace=True)
    X_train = pd.concat([X_train, X_train_scaled], axis=1)
    

    # Concatenate scaled test data onto sparse matrix
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate[['watchers_num', 'stars_num',
                                                            'forks_num', 'commits_num']]))
    X_validate_scaled.rename(columns={0: 'watchers_num',
                                   1: 'stars_num',
                                   2: 'forks_num',
                                   3: 'commits_num'},
                         inplace=True)
    
    X_validate_scaled.index = X_validate.index
    X_validate.drop(columns=['watchers_num', 'stars_num', 'forks_num', 'commits_num'], inplace=True)
    X_validate = pd.concat([X_validate, X_validate_scaled], axis=1)
    
    
    
    # Concatenate scaled test data onto sparse matrix
    X_test_scaled = pd.DataFrame(scaler.transform(X_test[['watchers_num', 'stars_num',
                                                          'forks_num', 'commits_num']]))
    
    X_test_scaled.rename(columns={0: 'watchers_num',
                                  1: 'stars_num',
                                  2: 'forks_num',
                                  3: 'commits_num'},
                         inplace=True)

    X_test_scaled.index = X_test.index
    X_test.drop(columns=['watchers_num', 'stars_num', 'forks_num', 'commits_num'], inplace=True)
    X_test = pd.concat([X_test, X_test_scaled], axis=1)
    
    return X_train, X_validate, X_test
