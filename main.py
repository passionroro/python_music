import numpy as np
import matplotlib.pyplot as plt
from pprintpp import pprint as pp
from scipy.io.wavfile import write

samplerate = 44100

def	get_wave(freq, duration=0.1):
	amplitude = 4096
	time = np.linspace(0, duration, int(samplerate * duration))
	wave = amplitude * np.sin(2 * np.pi * freq * time)

	return wave

def	get_piano_notes():
	octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
	base_freq = 261.63

	note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}
	note_freqs[''] = 0.0

	return note_freqs

def get_song_data(music_notes):
	note_freqs = get_piano_notes()
	song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
	song = np.concatenate(song)
	
	return song

music_notes = 'C-E-A--C-E-A--C-E-A--C-E-A--C-E-A--C-E-A--C-E-A--C-E-A--B-E-A--B-E-A--B-E-A--B-E-G--B-E-G--B-E-G--B-E-G--B-E-G'
data = get_song_data(music_notes)

write('still-dre.wav', samplerate, data.astype(np.int16))
