#!/usr/bin/env bash

# This one installs the new conda environment
echo "Creating the deepspeech conda environment"
echo "To activate this environment next time to run the speech2text, type source activate deepspeech"
sudo echo #So that it makes installation easier later

conda create --name deepspeech python=2.7 --yes
source activate deepspeech
conda install pandas --yes
conda install -c anaconda scipy --yes
conda install -c anaconda pip --yes
conda install -c anaconda gcc --yes
conda install -c anaconda swig --yes
conda install -c conda-forge importlib --yes
conda install -c anaconda requests --yes
yes | pip install deepspeech-gpu


#install prerequisites for training
yes | pip install -r requirements.txt

#So that you can train, specific version of tensorflow-gpu
cd DeepSpeech
python util/taskcluster.py --target /tmp --source tensorflow --arch gpu --artifact tensorflow_gpu_warpctc-1.4.0-cp27-cp27mu-linux_x86_64.whl
yes | pip install /tmp/tensorflow_gpu_warpctc-1.4.0-cp27-cp27mu-linux_x86_64.whl


#build the native-client
python util/taskcluster.py --target native-client/
cd ..

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


#this one gets some training data
python DeepSpeech/bin/import_cv.py data/common_voice/
