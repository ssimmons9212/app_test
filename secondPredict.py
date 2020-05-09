import pickle  
import FirstPrediction

# wrf = joblib.load('data/wrf_wne.joblib')
wrf = pickle.load(open('static/data/finalized_model.sav','rb'))

def SecondPredict(modelIn):
    X = [modelIn]
    p2 = wrf.predict(X)
    return p2 

# wrf = joblib.load('wrf_wne.joblib')
