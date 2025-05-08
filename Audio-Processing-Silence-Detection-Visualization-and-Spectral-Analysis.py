import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import soundfile as sf
fs = 8000
duration = 12

print("Recording")

recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
sd.wait()

print("Recording finished.")
wav.write("C:/Users/Asus/Desktop/sentence.wav", fs, recording)


import librosa
import librosa.display
import matplotlib.pyplot as plt
import os
FRAME_LENGTH_MS=30
FRAME_SHIFT_MS=10
signal,sr=librosa.load("C:/Users/Asus/Desktop/sentence.wav",sr=8000)
frame_length=int(fs*FRAME_LENGTH_MS/1000)
frame_shift=int(fs*FRAME_SHIFT_MS/1000)
frames = librosa.util.frame(signal, frame_length=frame_length, hop_length=frame_shift)




output_folder = "frames_waveforms"
os.makedirs(output_folder, exist_ok=True)

for i, frame in enumerate(frames):
    plt.figure(figsize=(8, 4))
    librosa.display.waveshow(frame, sr=sr)
    plt.title(f"Waveform of Frame {i+1}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.savefig(os.path.join(output_folder, f"frame_{i+1}.png"))
    plt.close()




print(f"{sr}")
plt.figure(figsize=(10, 6))
plt.plot(signal)
plt.title('Waveform')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
import librosa
import librosa.display
import matplotlib.pyplot as plt

file_path = "C:/Users/Asus/Desktop/sentence.wav"
signal, sample_rate = librosa.load(file_path, sr=8000) 
print(f"{sample_rate}")
# Plot mel-spectrogram
mel_spectrogram = librosa.feature.melspectrogram(y=signal, sr=sample_rate)
librosa.display.specshow(librosa.power_to_db(mel_spectrogram, ref=np.max), y_axis='mel', fmax=8000, x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel-Spectrogram')
plt.show()



zero_crossing_rate = librosa.feature.zero_crossing_rate(signal, frame_length=frame_length , hop_length=frame_shift)
print(" zero_crossing_rate :", zero_crossing_rate)


frame_length_ms = 30  
frame_shift_ms = 10   
frame_length = int((frame_length_ms / 1000) * sample_rate) 
frame_shift = int((frame_shift_ms / 1000) * sample_rate)   

# Calculate energy for each frame
energy = []
for i in range(0, len(signal) - frame_length + 1, frame_shift):
    frame = signal[i:i+frame_length]
    frame_energy = np.sum(frame ** 2)
    energy.append(frame_energy)

time = np.arange(len(energy)) * (frame_shift_ms / 1000)






threshold = 0.02
speech_regions = []
silence_regions = []

is_speech = False
start = 0
for i, e in enumerate(energy):
    if e > threshold:
        if not is_speech:
            if i - start >= 10:
                silence_regions.append((start, i))
                start = i
                is_speech = True
    else:
        if is_speech:
            if i - start >= 5:
                speech_regions.append((start, i))
                start = i
                is_speech = False

if is_speech:
    if len(energy) - start >= 5: 
        speech_regions.append((start, len(energy)))
else:
    if len(energy) - start >= 10:
        silence_regions.append((start, len(energy)))
speech_segments = [signal[start:end] for start, end in speech_regions]

print("Speech Regions:")
for region in speech_regions:
    print(f"Start: {region[0] * frame_shift_ms} ms, End: {region[1] * frame_shift_ms} ms")

print("\nSilence Regions:")
for region in silence_regions:
    print(f"Start: {region[0] * frame_shift_ms} ms, End: {region[1] * frame_shift_ms} ms")




import matplotlib.pyplot as plt

time_signal = np.arange(len(signal)) / sample_rate
plt.figure(figsize=(12, 6))
plt.plot(time_signal, signal, color='b')
plt.title('Waveform with Speech and Silence Regions')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)


for region in speech_regions:
    start_time = region[0] * frame_shift_ms / 1000
    end_time = region[1] * frame_shift_ms / 1000
    plt.axvspan(start_time, end_time, color='green', alpha=0.3)

for region in silence_regions:
    start_time = region[0] * frame_shift_ms / 1000
    end_time = region[1] * frame_shift_ms / 1000
    plt.axvspan(start_time, end_time, color='red', alpha=0.3)

plt.show()
