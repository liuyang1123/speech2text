#this module provides the functions to extract audio from videos

import subprocess
import os
import sys
# Pre...


def main(videos_path):
    files_list = {str(file): videos_path + file for file in os.listdir(videos_path)}

    # Extract audio from video.
    # It already save the video file using the named defined by output_name.
    for file_name,file_path_input in files_list.items():
        # Get the file name without extension
        if 'mouthcropped' not in file_name:
            raw_file_name = os.path.basename(file_name).split('.')[0]
            file_dir = os.path.dirname(file_path_input)
            file_path_output = file_dir + '/' + raw_file_name + '.wav'
            print('processing file: %s' % file_path_input)
            subprocess.call(
                ['ffmpeg', '-i', file_path_input, '-codec:a', 'pcm_s16le', '-ac', '1', file_path_output])
            print('file %s saved' % file_path_output)

if __name__ == '__main__':
    videos_path = raw_input("Indicate the directory where the video(s) are located in")
    main(videos_path)