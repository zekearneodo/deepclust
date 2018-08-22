import scipy.signal as sg
import numpy as np
import logging

from tqdm import tqdm
from deepclust.stream import rosa

logger = logging.getLogger('deepclust.stream.spectral')

def make_butter_bandpass(s_f, lo_cut, hi_cut, order=5):
    nyq = 0.5 * s_f
    low = lo_cut / nyq
    high = hi_cut / nyq
    b, a = sg.butter(order, [low, high], btype='band')
    return {'b': b, 'a': a}

def apply_butter_bandpass(x, pars, axis=0):
    return sg.filtfilt(pars['b'], pars['a'], x, axis=axis)

def rosa_spectrogram(y, hparams):
    D = rosa._stft(rosa.preemphasis(y,hparams), hparams)
    S = rosa._amp_to_db(np.abs(D)) - hparams['ref_level_db']
    return rosa._normalize(S, hparams)

def inv_spectrogram(spectrogram, hparams):
    '''Converts spectrogram to waveform using librosa'''
    S = rosa._db_to_amp(rosa._denormalize(spectrogram, hparams) + hparams['ref_level_db'])  # Convert back to linear
    return rosa.inv_preemphasis(rosa._griffin_lim(S ** hparams['power'], hparams), hparams)          # Reconstruct phase


# Somehow these filteres worked, the ones above I am not sure.
# def make_butter_bandpass(s_f, lo_cut, hi_cut, order=4):
#     hp_b, hp_a = sg.butter(order, lo_cut / (s_f / 2.), btype='high')
#     lp_b, lp_a = sg.butter(order, hi_cut / (s_f / 2.), btype='low')
#     return {'lo_cut': lo_cut,
#             'hi_cut': hi_cut,
#             'hp_b': hp_b,
#             'hp_a': hp_a,
#             'lp_b': lp_b,
#             'lp_a': lp_a}


# def apply_butter_bandpass(x, pars):
#     x_hi = sg.filtfilt(pars['hp_b'], pars['hp_a'], x, axis=0)
#     x_bp = sg.filtfilt(pars['lp_b'], pars['lp_a'], x_hi, axis=0)
#     return x_bp