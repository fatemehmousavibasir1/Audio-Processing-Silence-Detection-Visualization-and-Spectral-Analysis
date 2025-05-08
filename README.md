
#  Audio Processing: Silence Detection, Visualization, and Spectral Analysis

This project provides a full pipeline for recording, analyzing, and visualizing an audio signal, with a special focus on **frame-based energy calculation**, **silence and speech region detection**, and **spectral analysis** using **mel-spectrograms** and **zero-crossing rate**.

##  Features

-  Real-time audio recording via microphone (12 seconds at 8kHz)
-  Frame-wise energy computation with silence and speech segmentation
-  Mel-Spectrogram generation for frequency-based visualization
-  Per-frame waveform visualization and export
-  Zero-Crossing Rate analysis for signal noisiness or speech activity
-  Combined waveform visualization with speech/silence region highlighting


---

##  How It Works

1. **Recording**  
   Records a 12-second audio clip at 8000 Hz using your system's microphone and saves it as `sentence.wav`.

2. **Framing**  
   Splits the audio into short overlapping frames of 30 ms length and 10 ms shift (hop size).

3. **Energy Computation**  
   Computes the energy of each frame to distinguish **silent** vs **active** (speech) regions using a threshold.

4. **Speech/Silence Segmentation**  
   Marks consecutive frames with energy above/below the threshold as speech or silence segments respectively.

5. **Spectral Analysis**  
   Computes a **mel-spectrogram** to visualize the frequency content of the audio.

6. **Waveform Export**  
   Each frame is visualized and saved as an individual PNG file for further inspection.

7. **Final Visualization**  
   The full waveform is displayed with highlighted green (speech) and red (silence) areas.

---
