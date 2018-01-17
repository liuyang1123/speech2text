#!/usr/bin/env bash

# This one installs the new virtualenv environment
echo "Creating the deepspeech virtualenv environment"
echo "To activate this environment next time, type source ../deepspeech_interpreter/bin/activate"
sudo echo #So that it makes installation easier later

#get virtualenv
conda install -c anaconda pip --yes
yes | pip install virtualenv
#create the virtualenv
virtualenv --python=/usr/bin/python2.7 ../deepspeech_interpreter
#activate the virtualenv
source ../deepspeech_interpreter/bin/activate
# install
yes | pip install https://index.taskcluster.net/v1/task/project.deepspeech.deepspeech.native_client.master.gpu/artifacts/public/deepspeech_gpu-0.1.0-cp27-cp27mu-manylinux1_x86_64.whl
sudo apt-get install libcupti-dev --yes
#So that you can train, specific version of tensorflow-gpu. Please install the Cuda libraries yourself

#get the DeepSpeech repo
rm -r DeepSpeech -f
git clone git@github.com:mozilla/DeepSpeech.git
cd DeepSpeech
pip uninstall tensorflow --yes
python util/taskcluster.py --target /tmp --source tensorflow --arch gpu --artifact tensorflow_gpu_warpctc-1.4.0-cp27-cp27mu-linux_x86_64.whl
yes | pip install /tmp/tensorflow_gpu_warpctc-1.4.0-cp27-cp27mu-linux_x86_64.whl
yes | pip install -r requirements.txt
#build a GPU version native_client
python util/taskcluster.py --arch gpu --target native_client

cd ..




