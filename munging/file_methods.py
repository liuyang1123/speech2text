import os


def find_filetype(filepath):
    filetype = filepath.split('.')[-1].lower()
    return filetype


def find_filename(filepath):
    filename = filepath.split('/')[-1]
    return filename


def find_directory(filepath):
    if "/" in filepath:
        directory = filepath.replace(find_filename(filepath), "")
    else:
        directory = ""
    return directory


def prefix_filename(filepath, prefix):
    filename = find_filename(filepath)
    return filepath.replace(filename, str(prefix) + filename)


def find_directory__files(filepath, filetype=None):
    """
    Gets all the files in a directory as a dictionary of keys:values of file_name to file_path
    :param filepath: directory to get list of files from
    :param filetype: a filter of files to get
    :return:
    """

    sample_folder = filepath
    if filetype is None:
        files = {str(file_): sample_folder + file_ for file_ in os.listdir(sample_folder)}
    else:
        files = {str(file_): sample_folder + file_ for file_ in os.listdir(sample_folder) if file_.endswith(filetype)}

    return files
