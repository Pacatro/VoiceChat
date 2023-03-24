#!/bin/bash

toilet -f future 'WELCOME!'

echo -e "\nInstalling dependencies..."

#PyAudio
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg libav-tools
sudo pip install pyaudio

#Whisper
pip install -U openai-whisper
sudo apt update && sudo apt install ffmpeg

#ChatGPT RE
python -m pip install --upgrade revChatGPT

#gTTS
pip install gTTS

#Playsound
pip install playsound

#Wave
pip install Wave
