from __future__ import print_function
import scipy.io.wavfile as wavfile
from pydub import AudioSegment
import librosa
from munging.file_methods import prefix_filename, find_filetype
import os
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

    return audio_array, sample_rate


def convert_wavelength_file(filepath, wavelength, replace=True):
    """
    :param filepath: directory of file
    :param wavelength: new wavelength
    :param replace: whether to replace the file or make a file with prefix = new
    :return: prints out when the job is done
    """

    # since this is a conversion, we have to use librosa's library which is slower than scipy
    if not replace:
        filepath = prefix_filename(filepath, 'new_')
    # check whether it needs to be converted or not using scipy wav, faster load time
    sample_rate, audio_array = wavfile.read(filepath)

    if (sample_rate != wavelength) or (audio_array.dtype != np.int16):  # if not, then convert
        audio_array, sample_rate = librosa.load(filepath, sr=wavelength)
        maxv = np.iinfo(np.int16).max
        librosa.output.write_wav(filepath, (audio_array*maxv).astype(np.int16), sample_rate)
        print("The file", '"{}"'.format(filepath), "has been converted from", sample_rate, "to", wavelength)


def convert_mp3_to_wav(filepath, replace=False):
    """Converts mp3 to wav"""

    if find_filetype(filepath) != 'mp3':
        raise ValueError("This file isn't mp3")
    sound = AudioSegment.from_mp3(filepath)
    # convert mp3 to wav in filepath
    filepath_new = filepath.replace("mp3", "wav")

    sound.export(filepath_new, format="wav")

    if replace:
        # just delete the old mp3 file
        os.remove(filepath)
