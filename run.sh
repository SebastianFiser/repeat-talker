#!/bin/bash
#needed stuff to start the main file
source /home/sebastian/repeat\ talker/.venv/bin/activate
pip install -r requirements.txt
sudo apt install espeak-ng
python3 main.py