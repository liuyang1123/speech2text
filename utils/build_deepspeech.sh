#!/usr/bin/env bash

# This one installs the new virtualenv environment
echo "Building Deepspeech from source"
echo "Getting the GPU version for python programming"
sudo echo #So that it makes installation easier later

#remove the old one first
rm -r DeepSpeech/

#get latest Deepspeech
git clone git@github.com:mozilla/DeepSpeech.git
cd DeepSpeech
## remove git stuff
rm -f -r .git*

exit



