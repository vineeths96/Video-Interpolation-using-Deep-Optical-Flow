import imageio
import numpy as np
from os.path import *
from . import flow_utils

def read_gen(file_name):
    ext = splitext(file_name)[-1]
    if ext == '.png' or ext == '.jpeg' or ext == '.ppm' or ext == '.jpg' or ext == '.pgm':
        im = imageio.imread(file_name, as_gray=False, pilmode="RGB")
        return im
    elif ext == '.bin' or ext == '.raw':
        return np.load(file_name)
    elif ext == '.flo':
        return flow_utils.readFlow(file_name).astype(np.float32)
    return []
