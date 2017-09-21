import RPi.GPIO as GPIO
import time
from matrixQPi import *
import telepot
import Adafruit_CharLCD as LCD
from tkinter import *
import time
import os

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

#GPIO.output(LedPin, GPIO.HIGH)
#GPIO.setup(, GPIO.OUT)

lcd_columns = 16
lcd_rows = 2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(, GPIO.OUT)

keyPad=[[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
    ['*', 0, '#']
]

row=[7,0,2,3]
col=[12,5,6]

QPad  = matrixQPi(keyPad=keyPad,row=row,col=col)

numq = QPad.scanQ()

##########################################

GPIO.setup(19, GPIO.OUT)#motorfan
GPIO.setup(20, GPIO.OUT)#led
GPIO.setup(21, GPIO.OUT)#buz
GPIO.setup(10, GPIO.OUT)#motorswing
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)#ok button
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)#on/off fan


def botset(msg):
    chat_id = msg['chat']['id']
    command1 = msg['text1']
    print(msg['chat']['username'])
    print('Got command: %s' % command)
    if command == '/start':
            bot.sendMessage(chat_id_set, 'hi 'username'  thank you for using me you can see my options when you type /')
			lcd.message('you have started me')
	
    if command == '/on':
            
            bot.sendMessage(chat_id_set,'fan is on')			
            lcd.message('swing is on')
			time.sleep(5)
			lcd.clear()
			
	if command == '/off':
            
            bot.sendMessage(chat_id_set,'fan is off')			
            lcd.message('swing is off')
			time.sleep(5)
			lcd.clear()
		
			
	if command == '/swingon':
	        ##
			bot.sendMessage(chat_id_set,'swing is on')
			lcd.message('swing is on')
			time.sleep(5)
			lcd.clear()
	if command == '/swingoff':
	        ##
			bot.sendMessage(chat_id_set,'swing is off')
			lcd.message('swing is off')
			time.sleep(5)
			lcd.clear()
	if command == '/allon':
	        bot.sendMessage(chat_id_set,'swing and fan are on')
			lcd.message('swing and fan are on')
			time.sleep(5)
			lcd.clear()
            ##
    if command == 'alloff':
	        bot.sendMessage(chat_id_set,'swing and fan are off')
			lcd.message('swing and fan are off')
			time.sleep(5)
			lcd.clear()
            ##
    if command == '/settimeron':
            bot.sendMessage(chat_id_set,'set time to start fan example "5:14"')
			time.sleep(5)
    		hourstart=command1	
			lcd.message('timer set')
			time.sleep(5)
			lcd.clear()
			if setTime == hourstart:
			    lcd.message('start')
				time.sleep(5)
			    lcd.clear()
				
				bot.sendMessage(chat_id_set,'start')
            ##	
	if command == '/wakeupme' :
	        
			
		bot.sendMessage(chat_id_set,'when you want to wake up?')	
		time.sleep(5)
		wakeup=command1
	    if setTime==wakeup:
		    os.startfile('/home/pi/Desktop/cooler/1.mp4')
        	
      
    
bot = telepot.Bot('402342713:AAEjDah3pQkj84LvlQBr-1UJT0x9eLPn3Wg')
bot.message_loop(botset)


while 1:
    setTime = time.strftime('%I:%M')
	
    GPIO.output(21, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(21, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(21, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(21, GPIO.LOW)
	GPIO.output(20, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(20, GPIO.LOW)
	
	
	
    time.sleep(1)
	lcd.message('hi there')
	time.sleep(3)
	lcd.clear()
	lcd.message('im a smart fan!')
	time.sleep(2)	
	lcd.clear()
	lcd.message('you can control me with @smfnbot')
	time.sleep(6)
	lcd.clear()
	lcd.message('you must to enter your chat id')
	time.sleep(3)
	lcd.clear()
	lcd.message('chat id:)
	lcd.set_cursor(0,1)
	lcd.message(numq)
	if(GPIO.input() == 0):
	        chat_id_set=numq
			
