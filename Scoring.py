#This python file will keep track of blue alliance terminal scoring
#Imports
import serial

#Setup our serial connection
blue_ser = serial.Serial("COM3", 9600, timeout=1)

#Setup our game manager
waiting = True

while waiting == True:
    game_start = blue_ser.readline()
    
    if game_start == "game_time":
        game_running = True
        game_start = False

while game_running == True:
    data = blue_ser.readline()

    if data == "triangle":
        blue_score = blue_score + 4
        print("Blue scored triangle.")
    elif data == "circle":
        blue_score = blue_score + 3
        print("Blue scored circle.")
    elif blue_score == "square":
        blue_score = blue_score + 2
        print("Blue scored square.")