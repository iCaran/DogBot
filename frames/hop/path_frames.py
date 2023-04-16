import pickle

def get_points():
    with open('path_data.pkl', 'rb') as f:
        ends=pickle.load(f)
        return ends

def export_angles(t, k):
    with open('angles.pkl', 'wb') as f:
        # load each object from the file
        pickle.dump(t, f)
        pickle.dump(k, f)