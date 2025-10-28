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
#function for continuous recording and recognition
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
                    #přehrtí
                    subprocess.run(['espeak-ng', '-v', 'en-US', '-s 150', text])
                    # Zápis do souboru
                    with open(output_file, "a", encoding="utf-8") as f:
                        f.write(text + "\n")

                except sr.UnknownValueError:
                    print("Neporozuměl jsem, zkuste znovu.")
                except sr.RequestError as e:
                    print(f"Chyba připojení k Google API: {e}")
            except KeyboardInterrupt:
                print("\nUkončuji poslouchání…")
                sys.exit(0)

if __name__ == "__main__":
    record_continuous(language="en-US") #chenge depending on your language