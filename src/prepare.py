import pandas as pd
import numpy as np

import os
import unicodedata
import re
import json

import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def clean_language(df):
    '''
    This function takes the language column,
    strips the percentage numbers on the end
    and adds the plus signs to C
    '''
    df.language = df.language.str.replace(r'[\d+\.]', '')
    df.language = df.language.str.replace('C', 'C++')
    df.language = df.language.str.strip()
    return df

def clean_numeric_columns(df):
    '''
    This function takes the stars, commit and forks columns,
    strips them to only numbers,
    and changes the type to integer
    '''
    numeric_columns = ['stars', 'commits', 'forks']

    for column in numeric_columns:
        df[column] = df[column].astype('string')
        df[column] = df[column].str.replace('k', '00')
        df[column] = df[column].str.replace(r'[,.]', '')
        df[column] = df[column].astype(np.int)   
    return df


def basic_clean(string):
    '''
    This function takes in a string and
    returns the string normalized.
    '''
    string = unicodedata.normalize('NFKC', string.strip())\
             .encode('ascii', 'ignore')\
             .decode('utf-8', 'ignore')
    string = re.sub(r'[^\w\s]', '', string).lower()
    
    return string

##############################

def tokenize(string):
    '''
    This function takes in a string and
    returns a tokenized string.
    '''
    # Create tokenizer.
    tokenizer = ToktokTokenizer()
    
    # Use tokenizer
    string = tokenizer.tokenize(string, return_str=True)
    
    return string

#############################

def stem(string):
    '''
    This function takes in a string and
    returns a string with words stemmed.
    '''
    # Create porter stemmer.
    ps = PorterStemmer()
    
    # Use the stemmer to stem each word in the list of words we created by using split.
    stems = [ps.stem(word) for word in string.split()]
    
    # Join our lists of words into a string again and assign to a variable.
    string = ' '.join(stems)
    
    return string

#############################


def lemmatize(string):
    '''
    This function takes in string for and
    returns a string with words lemmatized.
    '''
    # Create the lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    
    # Use the lemmatizer on each word in the list of words we created by using split.
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # Join our list of words into a string again and assign to a variable.
    string = ' '.join(lemmas)
    
    return string

#############################


def remove_stopwords(string, extra_words=[], exclude_words=[]):
    '''
    This function takes in a string, 
    optional extra_words and exclude_words parameters
    with default empty lists and returns a string.
    '''
    # Create stopword_list.
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)

    # Add in 'extra_words' to stopword_list.
    stopword_list = stopword_list.union(set(extra_words))
    
    # Split words in string.
    words = string.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords

###############################


def prep_readme_data(df, column='readme', extra_words=[], exclude_words=[], explore=True):
    '''
    This function take in a df and the string name for a text column with 
    option to pass lists for extra_words and exclude_words and
    returns a df with the text article title, original text, stemmed text,
    lemmatized text, cleaned, tokenized, & lemmatized text with stopwords removed.
    '''
    df = clean_language(df)
    df = clean_numeric_columns(df)
    
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)\
                            .apply(lemmatize)
    
    df['stemmed'] = df[column].apply(basic_clean).apply(stem)
    
    df['lemmatized'] = df[column].apply(basic_clean).apply(lemmatize)
    
    words = [re.sub(r'([^a-z0-9\s]|\s.\s)', '', str(doc)).split() for doc in df.clean]
    
    df = pd.concat([df, pd.DataFrame({'words': words})], axis=1)
    
    df = df[['language', column, 'lemmatized', 'clean', 'words', 'watchers', 'stars', 'forks', 'commits']]
    
    tfidf = TfidfVectorizer()
    X_tfidf = tfidf.fit_transform(df.readme)
    X = pd.concat([df, pd.DataFrame(X_tfidf.todense())], axis=1)
    y = df.language
    
    X_train_validate, X_test, y_train_validate, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=1)
    X_train, X_validate, y_train, y_validate = train_test_split(X_train_validate, y_train_validate, stratify=y_train_validate, test_size=0.25, random_state=1)
    
    if explore == True:
        train = pd.concat([X_train, y_train], axis=1)
        return train[['language', 'clean', 'words', 'watchers', 'stars', 'forks', 'commits']]
    else:
        return X_train, y_train, X_validate, y_validate, X_test, y_test


def clean_explore(text):
    '''
    A simple function to cleanup text data in preparation of exploration
    '''
    ADDITIONAL_STOPWORDS = ['r', 'u', '2', 'ltgt']
    wnl = nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english') + ADDITIONAL_STOPWORDS
    text = (unicodedata.normalize('NFKD', text)
             .encode('ascii', 'ignore')
             .decode('utf-8', 'ignore')
             .lower())
    words = re.sub(r'[^\w\s]', '', text).split()
    return [wnl.lemmatize(word) for word in words if word not in stopwords]