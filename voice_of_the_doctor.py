#step1a:setup Text to speech-TTS-model gTTs

import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text,output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text = "hi this is rohit chandra pre-final year student from computer science specializing in artificial inteligence and machine learning at sathyabama Institute of science and technology."
#text_to_speech_with_gtts_old(input_text=input_text,output_filepath="gtts_testing.mp3")

#step1b:setup Text to speech-TTS-model Elevenlabs

import elevenlabs
from elevenlabs.client import ElevenLabs
ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    if not ELEVENLABS_API_KEY:
        print("Error: ELEVENLABS_API_KEY not found!")
        return
    
    print(f"Using API key: {ELEVENLABS_API_KEY[:10]}...")
    
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="pNInz6obpgDQGcFmaJgB",
        output_format="mp3_22050_32",
        model_id="eleven_turbo_v2"
    )
    
    with open(output_filepath, 'wb') as f:
        for chunk in audio:
            f.write(chunk)

input_text = "hi this is rohit chandra pre-final year student from computer science specializing in artificial inteligence and machine learning at sathyabama Institute of science and technology."
#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

#step2:use model model for text output to voice
import subprocess
import platform
import pygame

def text_to_speech_with_gtts(input_text,output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name=platform.system()
    try:
        if os_name=="Darwin":
            subprocess.run(['afplay',output_filepath])
        elif os_name=="Windows":
            #subprocess.run(['powershell','-c',f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            pygame.mixer.init()
            pygame.mixer.music.load(output_filepath)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)
            pygame.mixer.quit()
        elif os_name=="Linux":
            subprocess.run(['aplay',output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occured while trying to play the audio:{e}")

input_text = "hi this is rohit chandra pre-final year student from computer science specializing in artificial inteligence and machine learning at sathyabama Institute of science and technology.version 2.0"
text_to_speech_with_gtts(input_text=input_text,output_filepath="gtts_testing_2o.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    if not ELEVENLABS_API_KEY:
        print("Error: ELEVENLABS_API_KEY not found!")
        return
    
    print(f"Using API key: {ELEVENLABS_API_KEY[:10]}...")
    
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="pNInz6obpgDQGcFmaJgB",
        output_format="mp3_22050_32",
        model_id="eleven_turbo_v2"
    )
    
    with open(output_filepath, 'wb') as f:
        for chunk in audio:
            f.write(chunk)
    os_name=platform.system()
    try:
        if os_name=="Darwin":
            subprocess.run(['afplay',output_filepath])
        elif os_name=="Windows":
            #subprocess.run(['powershell','-c',f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            pygame.mixer.init()
            pygame.mixer.music.load(output_filepath)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)
                pygame.mixer.quit()
        elif os_name=="Linux":
            subprocess.run(['aplay',output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occured while trying to play the audio:{e}")

input_text = "hi this is rohit chandra pre-final year student from computer science specializing in artificial inteligence and machine learning at sathyabama Institute of science and technology.version 2.o"
text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_2o.mp3")