#!/usr/bin/env python3
import os
import sys
import speech_recognition as sr
import ctypes
import ctypes.util
import subprocess



# clearing ALSA a JACK lines
libc = ctypes.CDLL(ctypes.util.find_library('c'))
stderr_fileno = 2
devnull = os.open(os.devnull, os.O_WRONLY)
libc.dup2(devnull, stderr_fileno)
# end clearing

def wait_for_wake_word(wake_word="start listening", language="en-US", mic_index=None):
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=mic_index)
    print(f"Say '{wake_word}' to start listening...")

    with mic as source:
        r.adjust_for_ambient_noise(source)
        while True:
            try:
                audio = r.listen(source, timeout=None, phrase_time_limit=3)
                try:
                    text = r.recognize_google(audio, language=language).lower()
                    print(f"Heard: {text}")
                    if wake_word in text:
                        print("Wake word detected!")
                        return
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    print(f"Error connecting to Google API {e}")
            except KeyboardInterrupt:
                print("\nStopped by user.")
                sys.exit(0)

def record_continuous(language="en-US", mic_index=None, output_file="output.txt"):
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=mic_index)

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening started. Press Ctrl+C to stop.")

        while True:
            try:
                audio = r.listen(source, timeout=None, phrase_time_limit=None)
                try:
                    text = r.recognize_google(audio, language=language)
                    print(f"You said: {text}")
                    subprocess.run(['espeak-ng', '-v', 'en-US', '-s', '150', text])
                    with open(output_file, "a", encoding="utf-8") as f:
                        f.write(text + "\n")
                except sr.UnknownValueError:
                    print("I didn't get that, please try again.")
                except sr.RequestError as e:
                    print(f"Error connecting to Google API {e}")
            except KeyboardInterrupt:
                print("\nListening stopped by user.")
                sys.exit(0)
def play_start_sound(sound_path):
    try:
        subprocess.run(['aplay', sound_path], check=True)
    except Exception as e:
        print(f"Error playing sound: {e}")

if __name__ == "__main__":
    wait_for_wake_word(wake_word="start listening", language="en-US")
    sound_path = "./cat_meow.wav"
    play_start_sound(sound_path)
    record_continuous(language="en-US")