#This python file will keep track of blue alliance terminal scoring
#Imports
import serial
import time
from playsound import playsound

#Setup our serial connection
blue_ser = serial.Serial("COM2", 9600, timeout=1)
red_ser = serial.Serial("COM3", 9600, timeout=1)
mid_ser = serial.Serial("COM4", 9600, timeout=1)

#Setup our game manager
waiting = True

while waiting == True:
    game_start = blue_ser.readline()
    
    if game_start == "game_time":
        game_running = True
        waiting = False

game_running = True
playsound("audio/start.wav")
start_time = time.time()
while game_running == True:
    end_time = time.time()
    if end_time - start_time >= 120:
        break
    
    if end_time - start_time >= 90 and end_time - start_time <= 90.1:
        playsound("audio/resume.wav")

    blue_data = blue_ser.readline()
    red_data = red_ser.readline()
    mid_data = mid_ser.readline()

    if blue_data == "triangle":
        blue_score = blue_score + 4
        print("Blue scored triangle.")
    elif blue_data == "circle":
        blue_score = blue_score + 3
        print("Blue scored circle.")
    elif blue_data == "square":
        blue_score = blue_score + 2
        print("Blue scored square.")

    if red_data == "triangle":
        red_score = red_score + 4
        print("Red scored triangle.")
    elif red_data == "circle":
        red_score = red_score + 3
        print("Red scored circle.")
    elif red_data == "square":
        red_score = red_score + 2
        print("Red scored square.")

    if mid_data == "blue_mid":
        blue_score = blue_score + 1
        print("Blue scored mid.")
    elif mid_data == "red_mid":
        red_score = red_score + 1

playsound("audio/end.wav")