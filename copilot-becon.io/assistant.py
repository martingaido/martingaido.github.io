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
			mario_speak(ask)
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
		voice_data = r.recognize_google(audio, language='es').lower()
		print(voice_data)
	except sr.UnknownValueError:
		mario_speak("Lo siento, no entiendo el comando.")
	except sr.RequestError as e:
		mario_speak("El servicio no se encuentra disponible; {0}".format(e))
	return voice_data

def mario_speak(audio_string):
	tts = gTTS(text=audio_string, lang='es')
	r = random.randint(1, 10000000)
	audio_file = 'tmp-audio-' + str(r) + '.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)

def respond(voice_data):

	if 'cómo es tu nombre' in voice_data:
		mario_speak('Mi nombre es copiloto') # armar un array de respuestas y sacar una random
	if 'cómo te llamas' in voice_data:
		mario_speak('Mi nombre es copiloto')
	if 'cuál es tu nombre' in voice_data:
		mario_speak('Mi nombre es copiloto')

	if 'cómo es mi nombre' in voice_data:
		ask_back = record_audio('No lo sé, dime tu nombre asi lo puedo recordar la próxima vez.')
		mario_speak('Perfecto, asi que tu nombre es ' + ask_back + ', gusto en conocerte!')
	if 'cómo me llamo' in voice_data:
		ask_back = record_audio('No lo sé, dime tu nombre asi lo puedo recordar la próxima vez.')
		mario_speak('Perfecto, asi que tu nombre es' + ask_back + ', gusto en conocerte!')

	if 'qué hora es' in voice_data:
		mario_speak(ctime())
	if 'cuál es la hora' in voice_data:
		mario_speak(ctime())
	if 'decime la hora' in voice_data:
		mario_speak(ctime())
	if 'dime la hora' in voice_data:
		mario_speak(ctime())

	if 'necesito ayuda' in voice_data:
		mario_speak('este contenido no esta disponible por el momento')
	if 'dónde estoy' in voice_data:
		mario_speak('el contenido de ubicación no se encuentra disponible por el momento')
	if 'puntos de interés' in voice_data:
		mario_speak('el contenido de ubicación y puntos de interés no se encuentra disponible por el momento')
	if 'estaciones de metro' in voice_data:
		mario_speak('no hay información disponible sobre las estaciones de metro por el momento')
	if 'cómo está el clima' in voice_data:
		mario_speak('por el momento no puedo obtener datos del clima, intenta mas tarde')
	if 'voy a salir' in voice_data:
		mario_speak('bueno Martin, ten mucho cuidado y abrígate bien que hace frío')
	if 'tomar una foto' in voice_data:
		mario_speak('hecho, he tomado una foto de este momento y ha sido enviada a tu archivo')
	if 'distancia del objetivo' in voice_data:
		mario_speak('todavía no tengo conectado el laser para realizar esta medición')
	if 'enviar mensaje' in voice_data:
		mario_speak('no puedes realizar esta operación por el momento, intenta mas tarde')
	if 'leer mensajes nuevos' in voice_data:
		mario_speak('no puedes realizar esta operación por el momento, intenta mas tarde')
	if 'leer noticias' in voice_data:
		mario_speak('no puedes realizar esta operación por el momento, intenta mas tarde')
	if 'reconocer texto' in voice_data:
		mario_speak('cuando me conecten la cámara voy a poder realizar esta tarea')
	if 'reconocer objeto' in voice_data:
		mario_speak('cuando me conecten la cámara voy a poder realizar esta tarea')
	if 'estado del sistema' in voice_data:
		mario_speak('por ahora funciona todo bien, si hay alguna novedad estarás al tanto')
	if 'cambiar asistente' in voice_data:
		mario_speak('por ahora soy la única disponible, ¿no te gusta mi voz?')
	if 'tengo una emergencia' in voice_data:
		mario_speak('mas adelante vamos a detallar las opciones disponibles')
	if 'modo entrenamiento' in voice_data:
		mario_speak('haz iniciado el modo de entrenamiento pero por el momento no esta desarrollado')
	if 'lenguaje de señas' in voice_data:
		mario_speak('haz iniciado el intérprete de señas pero por el momento no esta desarrollado')
	if 'calendario' in voice_data:
		mario_speak('no tienes eventos en el calendario el día de hoy, mañana tienes dos eventos')
	if 'agregar nota' in voice_data:
		mario_speak('no puedo procesar esta información por el momento')
	if 'leer notas' in voice_data:
		mario_speak('no puedo procesar esta información por el momento')
	if 'agregar evento' in voice_data:
		mario_speak('no puedo procesar esta información por el momento')


	# if 'show me the news' in voice_data:
	# 	# connect to api
	# 	json_data = requests.get('http://newsapi.org/v2/everything?q=bitcoin&from=2020-05-07&sortBy=publishedAt&apiKey=0516986e36f24652926878343df151f0').json()
	# 	# json_data = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

	# 	for each in json_data['articles']:
	# 		# print(each['title'])
	# 		mario_speak(each['title'])
	# if 'search' in voice_data:
	# 	search = record_audio('What do you want to search?')
	# 	url = 'https://google.com/search?q=' + search
	# 	webbrowser.get().open(url)
	# 	mario_speak('Here is what I found for ' + search)
	# if 'find location' in voice_data:
	# 	location = record_audio('What is the location?')
	# 	url = 'https://google.nl/maps/place/' + location + '/&amp;'
	# 	webbrowser.get().open(url)
	# 	mario_speak('Here is the location of ' + location)

	if 'salir' in voice_data:
		mario_speak('Gracias por usar el Copiloto, nos vemos luego!')
		exit()
	if 'cancelar' in voice_data:
		mario_speak('Gracias por usar el Copiloto, nos vemos luego!')
		exit()

time.sleep(1)
mario_speak('Hola Martin, dime lo que necesitas y trataré de ayudarte!')
while 1:
	voice_data = record_audio()
	respond(voice_data)
