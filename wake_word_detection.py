import pvporcupine
import pyaudio

def wake_word_detection():
    porcupine = pvporcupine.create(keywords=["jarvis"])
    audio_stream = pyaudio.PyAudio().open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    while True:
        audio_data = audio_stream.read(porcupine.frame_length)
        if porcupine.process(audio_data) >= 0:
            print("Wake word detected!")
            break
