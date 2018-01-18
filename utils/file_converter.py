""" This thing takes a directory and converts all the files"""
from munging.preprocessing import convert_wavelength_file, convert_mp3_to_wav
from munging.file_methods import find_filetype, find_directory__files
import os


def main(directory, wavelength=16000, replace=True):
    """
    accepts either a file or a directory
    converts them to wav format and the specified wavelength with or without replacement
    """

    if os.path.isdir(directory):
        # get the directory of mp3 files
        mpthree_files = find_directory__files(directory, 'mp3')

        # check whether there are mp3 files
        if len(mpthree_files) > 0:
            # converts all the mp3 files to wav files
            map(lambda x: convert_mp3_to_wav(x, replace=replace), mpthree_files.values())

        # now get the wav files after conversion(if any)
        wav_files = find_directory__files(directory, 'wav')

        # convert
        map(lambda x: convert_wavelength_file(x, wavelength=wavelength, replace=replace), wav_files.values())
    elif os.path.isfile(directory):

        # check if it's a wav
        filetype = find_filetype(directory)
        if filetype != 'wav':
            if filetype == 'mp3':
                convert_mp3_to_wav(directory, replace=replace)
                # get the new file name
                directory = directory.replace('mp3', 'wav')
            else:
                raise ValueError("Not a supported filetype at this moment")

        # when filetype == wav or after converting from mp3 to wav
        convert_wavelength_file(directory, wavelength, replace=replace)
    else:
        raise ValueError("input is wrong")


# When this is run standalone
if __name__ == '__main__':
    file_convert = raw_input("file/directory to be converted: ")
    main(file_convert)
