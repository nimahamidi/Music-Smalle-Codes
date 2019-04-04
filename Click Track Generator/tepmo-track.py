import numpy as np
import librosa 

from pydub import AudioSegment

def click_maker (file_name, tempo):
    audio = "edited.wav"
    click, sr = librosa.load(audio)
    duration = len(click)/sr
    silence = tempo - duration
    click_final = np.zeros(int(tempo * sr))
    click_final[:len(click)] = click
    return click_final, sr

def make_click_track (tempoes):
    click_track = []
    for i in range (len(tempoes)):
        click, sr = click_maker ("click.wav", tempoes[i])
        click_track =  np.append (click_track, click)
    return click_track, sr

tempoes = [2.43, 4.21, 1.33, 3.12, 2.11]
click_track, sr = make_click_track (tempoes)
librosa.output.write_wav('Tempo Track.wav', click_track, sr)
