import os
import librosa
import torch
import numpy as np
from torch.utils.data import Dataset

class VoiceDataset(Dataset):
    def __init__(self, real_folder, fake_folder, max_duration=4, sr=16000):
        self.files = []
        self.labels = []
        self.sr = sr
        self.max_length = int(sr * max_duration)

        # Load Real Files (Label 1)
        for filename in os.listdir(real_folder):
            if filename.endswith(('.wav', '.mp3', '.flac')):
                self.files.append(os.path.join(real_folder, filename))
                self.labels.append(1)

        # Load Fake Files (Label 0)
        for filename in os.listdir(fake_folder):
            if filename.endswith(('.wav', '.mp3', '.flac')):
                self.files.append(os.path.join(fake_folder, filename))
                self.labels.append(0)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        # Load audio
        audio_path = self.files[idx]
        # Load with librosa (automatically resamples to 16kHz)
        audio, _ = librosa.load(audio_path, sr=self.sr)

        # Pad or Truncate to fixed length
        if len(audio) > self.max_length:
            audio = audio[:self.max_length]
        else:
            padding = self.max_length - len(audio)
            audio = np.pad(audio, (0, padding), mode='constant')

        return {
            "input_values": torch.tensor(audio, dtype=torch.float),
            "labels": torch.tensor(self.labels[idx], dtype=torch.long)
        }