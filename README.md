# Repeat Talker – Speech-to-Text & Text-to-Speech Assistant

## Overview

**Repeat Talker** is a Python-based assistant that:
- Waits for a wake word ("hey yuki" or "start listening"),
- Plays a customizable sound when activated,
- Listens to your microphone,
- Converts speech to text,
- Displays recognized text in the console,
- Saves each recognized sentence to `output.txt`,
- Repeats what you said using text-to-speech.

---

## Features

- **Wake Word:** Listening starts only after you say the wake phrase ("hey yuki" or "start listening").
- **Sound Notification:** Plays a sound when activated (customizable file).
- **Continuous Listening:** Keeps listening and processing speech until stopped.
- **Text Logging:** Every recognized sentence is saved to `output.txt`.
- **System Reply:** The system repeats your speech using text-to-speech.
- **Multilanguage Support:** Default is English (`en-US`), but you can change it.
- **Clean Output:** Suppresses ALSA/JACK errors.
- **Graceful Exit:** Stop anytime with `CTRL+C`.

---

## Requirements

- Python 3.13+
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [espeak-ng](https://github.com/espeak-ng/espeak-ng) (for text-to-speech, install via your system package manager)
- Microphone and sound system (ALSA/PulseAudio)
- Active internet connection (for Google Speech API)
- Optionally: [ffmpeg](https://ffmpeg.org/) (if you want to play non-WAV sound files)

Install Python dependencies:
```bash
pip install SpeechRecognition PyAudio
```
Install system tools:
```bash
sudo apt install espeak-ng alsa-utils ffmpeg
```

---

## Usage

1. Prepare a sound file for notification (e.g., `cat_meow.wav` or another).
2. Run the script:
    ```bash
    python3 main.py
    ```
3. Say the wake word ("hey yuki" or "start listening").
4. After the sound notification, speak into your microphone. The program will repeat your speech and save it to `output.txt`.
5. Stop the program with `CTRL+C`.

To change the language or sound file, edit these lines in `main.py`:
```python
wait_for_wake_word(wake_word="hey yuki", language="en-US")
sound_path = "./cat_meow.wav"
play_start_sound(sound_path)
record_continuous(language="en-US")
```

---

## File Structure

```
repeat talker/
│
├─ main.py          # main script for speech recognition and reply
├─ output.txt       # automatically generated text file
├─ cat_meow.wav     # sound file for notification (customizable)
└─ README.md        # this file
```

---

## Next Steps

- Support for multiple languages simultaneously.
- GUI for displaying text and managing settings.
- Offline speech recognition (no Google API).
- Customizable wake word and notification sounds.
- Selectable voice synthesizer.

---

## Troubleshooting

- If the sound does not play, check the file format (WAV for `aplay`, OGG/MP3 for `ffplay`).
- If the microphone does not work, check your device settings.
- Speech recognition issues may be caused by poor internet connection or incorrect language settings.

---

## License

MIT License
