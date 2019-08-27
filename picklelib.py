import pickle

def save_pickle(name, data):
    with open(name, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return 0

def get_pickle_info(name):
    with open(name, 'rb') as handle:
        data = pickle.load(handle)
    return data