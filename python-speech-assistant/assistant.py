#!/usr/bin/env python3

# https://pypi.org/
# https://pypi.org/project/SpeechRecognition/
# https://pypi.org/project/gTTS/
# https://pypi.org/project/playsound/ (play in console instead of itunes)
# https://pypi.org/project/pyobjc/
# https://github.com/Uberi/speech_recognition#readme
# brew install portaudio
# sudo pip3 install pyaudio

# news api key: 0516986e36f24652926878343df151f0

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import json
import requests
from gtts import gTTS
from time import ctime

# obtain audio from the microphone
r = sr.Recognizer()

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def record_audio(ask = False):
	with sr.Microphone(device_index=0) as source:
		if ask:
			assistant_speak(ask)
		# r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
		audio = r.listen(source)
		voice_data = ''

		## write recordings from user in audio to a WAV file
		## to location /recs
		# r1 = random.randint(1, 10000000)
		# with open('recs/microphone-rec-' + str(r1) + '.wav', 'wb') as f:
			# f.write(audio.get_wav_data())
			# os.remove('recs/microphone-rec-' + str(r1) + '.wav')

	# recognize speech using Google Speech Recognition
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		# print("You said: " + r.recognize_google(audio))
		voice_data = r.recognize_google(audio, language='en-US')
		print(voice_data)
	except sr.UnknownValueError:
		assistant_speak("Sorry, I did not get that.")
	except sr.RequestError as e:
		assistant_speak("Service not working; {0}".format(e))
	return voice_data

def assistant_speak(audio_string):
	tts = gTTS(text=audio_string, lang='en')
	r = random.randint(1, 10000000)
	audio_file = 'tmp-audio-' + str(r) + '.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)

def respond(voice_data):
	if 'what is your name' in voice_data:
		assistant_speak('My name is Susan')
	if 'what is my name' in voice_data:
		ask_back = record_audio('Don\'t know, but tell me so I can remember, what is your name?')
		assistant_speak('Got it, so your name is' + ask_back + ', nice to meet you!')
	if 'what time is it' in voice_data:
		assistant_speak(ctime())
	if 'show me the news' in voice_data:
		# connect to api
		json_data = requests.get('http://newsapi.org/v2/everything?q=bitcoin&from=2020-05-07&sortBy=publishedAt&apiKey=0516986e36f24652926878343df151f0').json()
		# json_data = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

		for each in json_data['articles']:
			# print(each['title'])
			assistant_speak(each['title'])
	if 'search' in voice_data:
		search = record_audio('What do you want to search?')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		assistant_speak('Here is what I found for ' + search)
	if 'find location' in voice_data:
		location = record_audio('What is the location?')
		url = 'https://google.nl/maps/place/' + location + '/&amp;'
		webbrowser.get().open(url)
		assistant_speak('Here is the location of ' + location)
	if 'exit' in voice_data:
		assistant_speak('Goodbye!')
		exit()
	if 'quit' in voice_data:
		assistant_speak('Goodbye!')
		exit()

time.sleep(1)
assistant_speak('How can I help you?')
while 1:
	voice_data = record_audio()
	respond(voice_data)
