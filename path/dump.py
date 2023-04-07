import pickle

def export(vars):
    with open('path_data.pkl', 'wb') as f:
        for i in vars:
            pickle.dump(i, f)