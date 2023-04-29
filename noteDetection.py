import statsmodels.api as sm
from scipy.signal import find_peaks
import audioCutter
import os
import librosa


def decode_binary_string(s):
  c = ''
  for i in s:
    c += i
  return ''.join(chr(int(c[i * 8:i * 8 + 8], 2)) for i in range(len(c) // 8))

def freq(sound):
  data, sampling_frequency = librosa.load(sound)
  auto = sm.tsa.acf(data, nlags=2000)
  peaks = find_peaks(auto)[0]  # Find peaks of the autocorrelation
  try:
    lag = peaks[0]
    pitch = sampling_frequency / lag
    return round(pitch)
  except:
    pass


count = audioCutter.split_audio()
print(count,'new files created')

message = ""
for i in range(0, count):
  t = freq(f'chunk{i}.wav')
  message += str(int(t > 433))

print(message)
message = decode_binary_string(message)
print("\nYour message:", message)

os.remove('0.wav')
for i in range(0, count):
  os.remove(f'chunk{i}.wav')
