from __future__ import absolute_import, division, print_function
from munging.preprocessing import standardized_read
from utils import file_converter
from munging.file_methods import find_directory__files
from deepspeech.model import Model
from json import load

sample_folder = 'data/samples/'

output_graph = 'models/trained/output_graph.pb'
alphabet = 'models/trained/alphabet.txt'
lm_binary = 'models/trained/lm.binary'
trie = 'models/trained/trie'

# configuration
with open('model_hyperparameters.json', 'rb') as f:
    config = load(f)

# These constants control the beam search decoder
# Beam width used in the CTC decoder when building candidate transcriptions
BEAM_WIDTH = config['BEAM_WIDTH']
standard_wavelength = config['standard_wavelength']

# The alpha hyperparameter of the CTC decoder. Language Model weight
LM_WEIGHT = config['LM_WEIGHT']

# The beta hyperparameter of the CTC decoder. Word insertion weight (penalty)
WORD_COUNT_WEIGHT = config['WORD_COUNT_WEIGHT']

# Valid word insertion weight. This is used to lessen the word insertion penalty
# when the inserted word is part of the vocabulary
VALID_WORD_COUNT_WEIGHT = config['VALID_WORD_COUNT_WEIGHT']

# These constants are tied to the shape of the graph used (changing them changes
# the geometry of the first layer), so make sure you use the same constants that
# were used during training

# Number of MFCC features to use
N_FEATURES = config['N_FEATURES']

# Size of the context window used for producing timesteps in the input vector
N_CONTEXT = config['N_CONTEXT']

if __name__ == '__main__':
    # preprocess the files, wavelengths and filetype within sample_folder
    file_converter.main(sample_folder)
    files = find_directory__files(sample_folder, 'wav')

    # create the model
    ds = Model(output_graph, N_FEATURES, N_CONTEXT, alphabet, BEAM_WIDTH)
    ds.enableDecoderWithLM(alphabet, lm_binary, trie, LM_WEIGHT, WORD_COUNT_WEIGHT, VALID_WORD_COUNT_WEIGHT)

    # dictionary comprehension to output
    prediction = {file_name: ds.stt(*standardized_read(directory, standard_wavelength))
                  for file_name, directory in files.items()
                  }
    print(prediction)

    # save the prediction, via addition into a text file, accumulate.
    with open('output.txt', 'w+') as f:
        f.write(str(prediction) + '\n')
        f.close()
