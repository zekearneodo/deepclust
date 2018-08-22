import numpy as np

def rms(x, axis=0):
    #print('plain rms with shape {}'.format(x.shape))
    if axis is None:
        return np.linalg.norm(x)
    else:
        return np.linalg.norm(x, axis=axis)/np.sqrt(x.shape[axis])