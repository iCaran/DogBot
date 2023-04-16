import pickle

def get_points():
    with open('angles.pkl', 'rb') as f:
        t=pickle.load(f)
        k=pickle.load(f)
        return t, k