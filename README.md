# speech2text

1. Please install CUDNN for tensorflow 1.4
2. Install Cuda toolkit for tensorflow 1.4
3. go to command line and clone this repo, then CD to it then run: 

		bash environ_install.sh
4. Learn to use virtualenv as we will standardize environments this way.


To run the virtualenv and the standardized interpreter, on command line:
	
		virtualenv ../deepspeech_interpreter/bin/activate

Once you activated the environment, then you can run python files properly.

### Getting the trained models
Before you can run anything, you need the trained models

1. Go to releases in the github repo page
2. find the latest one
3. Download
4. Extract into speech2text/models/trained/