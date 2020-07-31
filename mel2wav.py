import os

import numpy as np
from hparams import hparams
from datasets import audio

mel_dir = "tacotron_output/eval/"
files = os.listdir(mel_dir)
for file in files:
	if file[-3:] == "npy":
		path_file = os.path.join(mel_dir, file)
		mel_data = np.load(path_file)
		wav = audio.inv_mel_spectrogram(mel_data.T, hparams)
		wav_name = os.path.join("wavs/", file[:-3] + "wav")
		audio.save_wav(wav, wav_name, sr=22050)
