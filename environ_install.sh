#!/usr/bin/env bash

# This one installs the new conda environment
echo "Creating the deepspeech conda environment"
echo "To activate this environment next time to run the speech2text, type source activate deepspeech"
conda create --name deepspeech python=2.7 --yes
source activate deepspeech
conda install pandas --yes
conda install -c anaconda scipy --yes
conda install -c conda-forge tensorflow-gpu --yes
conda install -c anaconda pip --yes
yes | pip install deepspeech-gpu

#checks for OS since some tards use Mac

platform='unknown'
unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
   platform='linux'
elif [[ "$unamestr" == 'Darwin' ]]; then
   platform='mac'
fi
#then downloads some pre-built binaries
if [[ $platform == 'linux' ]]; then
   python DeepSpeech/util/taskcluster.py --target native-client/.
elif [[ $platform == 'mac' ]]; then
   python DeepSpeech/util/taskcluster.py --arch osx --target native-client/.
fi


#this one gets the pretrained models
wget -O - https://github.com/mozilla/DeepSpeech/releases/download/v0.1.0/deepspeech-0.1.0-models.tar.gz | tar xvfz -