from pydub import AudioSegment
from pydub.silence import split_on_silence

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

def split_again():
    counter = 0
    seconds = 100
    sCount = 0
    sound = AudioSegment.from_wav("0.wav")
    while counter < librosa.get_duration(path='0.wav') * 1000:
        audio = sound[counter:counter+seconds]
        audio.export(f'chunk{sCount}.wav')
        sCount += 1
        counter += 100

    return sCount


def split_audio():
    global speed_change
    #reading from audio mp3 file
    sound = AudioSegment.from_wav("output.wav")
    sound = speed_change(sound, 0.25)
    sound.export("output.wav", format="wav")
    # spliting audio files
    audio_chunks = split_on_silence(sound, min_silence_len=5, silence_thresh=-50)
    #loop is used to iterate over the output list
    for i, chunk in enumerate(audio_chunks):
       output_file = f"{i}.wav"
       print("Exporting file", output_file)
       chunk.export(output_file, format="wav")
       break

    a = split_again()

    return a
