
import scipy.io.wavfile as wavfile
from resampy import resample
import librosa
import numpy as np

def standardized_read(filepath,wavelength,replace=True):
    '''
    Makes sure that files are read and standardized to a certain wavelength specified with wavelength
    output: audio_array( either resampled or not), samplerate
    inputs:
     directory of file
    wavelength to standardize to

    '''
    SampleRate,audio_array = wavfile.read(filepath)
    #makes sure the sample rate == wavelength
    if SampleRate != wavelength:
        audio_array__resampled = resample(audio_array,SampleRate,wavelength)
        #if this doesn't work that means we need to load it as a float with librosa which is slowe




        #assumes that new wavelength is == wavelength
        return audio_array__resampled, wavelength
    return audio_array, SampleRate


def convert_wavelength(filepath,wavelength):


def convert_filetype(filepath):


def find_filetype(filepath):


