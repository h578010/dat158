import numpy as np
import pandas as pd
import joblib
import math

model = joblib.load('../boxoffice_model.joblib')

def preprocess(data):

    feature_values = {
        'budget': 8000000,
        'popularity': 7.4,          
        'runtime': 104,
        'has_collection': False,
        'has_homepage': False,
        'has_tagline': True,
        'titleMatch': True,
        'release_month': 9,
        'release_day': 1,
        'release_year': 2013,
        'orig_lang_en': True,
        'no_languages': 1,
        'no_genres': 2,
        'no_cast': 15
    }

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values

def predict(data):

    column_order = ['budget','popularity', 'runtime', 'has_collection', 'has_homepage', 'has_tagline', 'titleMatch', 'release_month', 'release_day', 'release_year', 'orig_lang_en', 
    'no_languages', 'no_genres', 'no_cast']

    # PREPROCESSING
    data['budget'] = math.log1p(data['budget'])
    data['popularity'] = math.log1p(data['popularity'])

    data = np.array([data[feature] for feature in column_order], dtype=object)

    pred = model.predict(data.reshape(1,-1))
    #uncertainty = model.predict_proba(data.reshape(1,-1))

    return pred

def postprocess(prediction):
    pred = prediction

    try: 
        int(pred[0]) > 0
    except:
        pass

    pred = math.expm1(pred)
    pred = str(int(pred))

    return_dict = {'pred': pred}

    return return_dict

