#!/usr/bin/env python3

# https://pypi.org/
# https://pypi.org/project/SpeechRecognition/
# https://pypi.org/project/gTTS/
# https://pypi.org/project/playsound/ (play in console instead of itunes)
# https://pypi.org/project/pyobjc/
# https://github.com/Uberi/speech_recognition#readme
# brew install portaudio
# sudo pip3 install pyaudio

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

# obtain audio from the microphone
r = sr.Recognizer()

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def record_audio(ask = False):
	with sr.Microphone(device_index=0) as source:
		if ask:
			mario_speak(ask)
		# r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
		audio = r.listen(source)
		voice_data = ''

	# recognize speech using Google Speech Recognition
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		# print("You said: " + r.recognize_google(audio))
		voice_data = r.recognize_google(audio)
		print(voice_data)
	except sr.UnknownValueError:
		mario_speak("Sorry, I did not get that.")
	except sr.RequestError as e:
		mario_speak("Service not working; {0}".format(e))
	return voice_data

def mario_speak(audio_string):
	tts = gTTS(text=audio_string, lang='en')
	r = random.randint(1, 10000000)
	audio_file = 'audio-' + str(r) + '.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)

def respond(voice_data):
	if 'what is your name' in voice_data:
		mario_speak('My name is Mario')
	if 'what time is it' in voice_data:
		mario_speak(ctime())
	if 'search' in voice_data:
		search = record_audio('What do you want to search?')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		mario_speak('Here is what I found for ' + search)
	if 'find location' in voice_data:
		location = record_audio('What is the location?')
		url = 'https://google.nl/maps/place/' + location + '/&amp;'
		webbrowser.get().open(url)
		mario_speak('Here is the location of ' + location)
	if 'exit' in voice_data:
		mario_speak('Goodbye!')
		exit()
	if 'quit' in voice_data:
		mario_speak('Goodbye!')
		exit()

time.sleep(1)
mario_speak('How can I help you?')
while 1:
	voice_data = record_audio()
	respond(voice_data)
