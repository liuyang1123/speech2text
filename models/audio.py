from pydub import AudioSegment
from pydub import silence


class Speech(object):
    def __init__(self, audio_array, sample_rate):
        self.audio_array = audio_array
        self.sample_rate = sample_rate
        self.speech = AudioSegment(data=self.audio_array, frame_rate=sample_rate)
        self.text = dict()

    def _segmentize_silence(self, min_silence_len=1000, silence_thresh=-16, keep_silence=100,
seek_step=1):
        self.segments = silence.split_on_silence(self.speech, min_silence_len=min_silence_len, silence_thresh=silence_thresh, keep_silence=keep_silence)

    def infer_speech(self, model_infer_func):
        self.text = model_infer_func(self.audio_array, self.sample_rate)