from __future__ import print_function
import scipy.io.wavfile as wavfile
import numpy as np


def standardized_read(filepath, wavelength):
    """Makes sure that files are read and standardized to a certain wavelength specified with wavelength
    output: audio_array( either resampled or not), samplerate
    inputs:
     directory of file
    wavelength to standardize to
    """

    sample_rate, audio_array = wavfile.read(filepath)
    # makes sure the sample rate == wavelength
    assert sample_rate == wavelength, "Only {} input WAV files are supported for now!".format(wavelength)
    # makes sure that the format of the audio array is np.int16
    assert audio_array.dtype == np.int16, "Only int16 audio files are supposed for now!"

    return audio_array, sample_rate

