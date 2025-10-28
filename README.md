Jasně, tady je čistá anglická verze README vhodná pro GitHub:

---

# Speech-to-Text Listener – Phase 1

## Overview

This project is a simple **speech-to-text system** that:

* continuously listens to your microphone,
* converts spoken words into text,
* displays recognized text in the console,
* saves each recognized sentence into `output.txt`.

Built in Python using the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library.

---

## Features

* **Continuous Listening:** Runs in a loop and automatically captures speech.
* **Multilanguage Support:** Default is English (`en-US`), but you can switch to any language supported by Google Speech API.
* **Text Logging:** Recognized text is appended to `output.txt`.
* **Clean Output:** Suppresses verbose ALSA/JACK errors.
* **System Reply** the system itself WILL repeat what you said
* **Graceful Exit:** Stop the program anytime with `CTRL+C`.

---

## Requirements

* Python 3.13+
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* Microphone and sound system (ALSA/PulseAudio)
* Active internet connection (for Google Speech API)

Install dependencies:

```bash
pip install SpeechRecognition #not needed because of run.sh
```

---

## Usage

1. Run the script:

```bash
run.sh
```

2. Speak into your microphone. The program will print recognized text and save it to `output.txt`.

3. Stop the program with `CTRL+C`.

4. To change the language, adjust the `language` parameter in `record_continuous`:

```python
record_continuous(language="en-US")  # for English
```

---

## File Structure

```
project_root/
│
├─ sTT.py          # main speech-to-text script
├─ output.txt      # automatically generated text file
└─ README.md       # this file
```

---

## Next Steps

* Add **support for multiple languages simultaneously**.
* Create a **GUI** to display text and manage microphone/language settings.
* Implement **offline recognition** without relying on Google API.

---

If you want, I can also make a **super concise GitHub-ready version**, short and polished, perfect for showcasing the project. Do you want me to do that?
