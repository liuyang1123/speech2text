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
sudo apt-get install libcupti-dev --yes



#install prerequisites
yes | pip install -r requirements.txt

#So that you can train, specific version of tensorflow-gpu

cd DeepSpeech
python util/taskcluster.py --target /tmp --source tensorflow --arch gpu --artifact tensorflow_gpu_warpctc-1.4.0-cp27-cp27mu-linux_x86_64.whl
yes | pip install /tmp/tensorflow_gpu_warpctc-1.4.0-cp27-cp27mu-linux_x86_64.whl

#build native client with gpu binary
python util/taskcluster.py --target . --arch gpu

cd ..
#finally install the thing
yes | pip install deepspeech-gpu

#this one gets the pretrained models
wget -O - https://github.com/mozilla/DeepSpeech/releases/download/v0.1.0/deepspeech-0.1.0-models.tar.gz | tar xvfz -


#this one gets some training data
python DeepSpeech/bin/import_cv.py data/
tar -xvzf data/cv_corpus_v1.tar.gz data/

