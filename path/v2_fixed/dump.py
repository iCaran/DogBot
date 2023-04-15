import pickle

def export(vars):
    with open('path_data.pkl', 'wb') as f:
       pickle.dump(vars, f)