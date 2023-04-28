import wave
from pydub import AudioSegment
from pydub.playback import play

word = input("enter a word: ")
word += word[-1]
wordBinary = ''.join(format(ord(i), '08b') for i in word)
letters = []

for i in wordBinary:
    print(i)
    if i == '0':
        letters.append(f'sineTones\\0.wav')
    else:
        letters.append(f'sineTones\\1.wav')


def concatenate_audio_wave(audio_clip_paths, output_path):

    data = []
    for clip in audio_clip_paths:
        w = wave.open(clip, "rb")
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
    output = wave.open(output_path, "wb")
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])

    print('Audio join complete')
    output.close()

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

concatenate_audio_wave(letters, 'output.wav')
audio = AudioSegment.from_file('output.wav', format='wav')
audio = speed_change(audio, 4)
audio.export("output.wav", format="wav")


