import os
import pickle

def save_stub(stub_path, object_to_save):
    if not os.path.exists(os.path.dirname(stub_path)):
        os.mkdir(os.path.dirname(stub_path))

    if stub_path is not None:
        # wb = write bytes
        with open(stub_path, 'wb') as f:
            pickle.dump(object_to_save, f)

def read_stub(read_from_stub, stub_path):
    if read_from_stub and stub_path is not None and os.path.exists(stub_path):
        # rb = read bytes
        with open(stub_path, 'rb') as f:
            object_to_read = pickle.load(f)
            return object_to_read
    return None