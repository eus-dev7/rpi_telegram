import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#Encendido y apagado de LED en el pin físico 40
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
	return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
	return

# Sistema de numeración de la Raspberry Pi 
GPIO.setmode(GPIO.BOARD)

# Configurar pin 40 como salida
GPIO.setup(40, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'On':
       bot.sendMessage(chat_id, on(40))
    elif command =='Off':
       bot.sendMessage(chat_id, off(40))

bot = telepot.Bot('392034817:AAHVGuFiL2z3uX9M5e9hc9OXXI-SUbS0GUc')
bot.message_loop(handle)
print 'I am listening...'

while 1:
	time.sleep(10)
