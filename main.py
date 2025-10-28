import subprocess

text = input("Enter text to speak: ")
subprocess.run(['espeak-ng', '-v', 'en+ja', '-s 150', text])
