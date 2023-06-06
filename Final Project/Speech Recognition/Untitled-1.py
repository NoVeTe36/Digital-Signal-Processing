# %%
import ipywidgets as widgets
from IPython.display import display
from threading import Thread
from queue import Queue
import pyaudio
import wave
import os
from time import sleep

p = pyaudio.PyAudio()
message = Queue()
recording = Queue()

CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2


# Create a button
record_button = widgets.Button(
    description="Record",
    disabled = False,
    button_style='info', 
    icon  = 'microphone'
)

stop_button = widgets.Button(
    description="Stop",
    disabled = False,
    button_style='warning',
    icon  = 'stop'
)

output = widgets.Output()

# %%
def record_audio( chunk = 1024):
    p = pyaudio.PyAudio()

    stream = p.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=FRAME_RATE,
                    input = True,
                    input_device_index = 12,
                    frames_per_buffer=chunk)
    
    global frames
    frames = []

    while not message.empty():
        data = stream.read(chunk)
        frames.append(data)

        if len(frames) >= (FRAME_RATE / chunk) * RECORD_SECONDS:
            recording.put(frames.copy())
            frames = []

    try:
        # delete the existing output file
        os.remove("output.wav")
    except:
        pass
    # Export to a wav file
    wf = wave.open("output.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(AUDIO_FORMAT))
    wf.setframerate(FRAME_RATE)
    wf.writeframes(b''.join(frames))

    stream.stop_stream()
    stream.close()
    p.terminate()

# %%
def start_record(data):
    message.put(True)
    with output:
        print("Recording...")
        record = Thread(target=record_audio)
        record.start()
        
        # transcribe = Thread(target=speech_recognition, args=(output,))
        # transcribe.start()

def stop_record(data):
    with output:
        message.get()
        display("Stop recording")

# %%
record_button.on_click(start_record)
stop_button.on_click(stop_record)

display(record_button, stop_button, output)

# %%
for i in range (p.get_device_count()):
    print(p.get_device_info_by_index(i))


