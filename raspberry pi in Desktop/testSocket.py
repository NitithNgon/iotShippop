import socket
import socketio

import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
from time import sleep
import requests
from pprint import pprint
import socketio

host =socket.gethostname()
host = '20.205.123.195'
port = '80'
sio = socketio.Client()

def main(host,port):
    sio.connect(f'http://{host}:{port}')
    sio.wait()

@sio.event
def connect():
    print("I'm connected!")  

@sio.on('sendstatus')
def activeCamera(status):
    if status==True:
        print('status:',status,'activeCamera')
        takePicture()
    if status==False:
        print('status:',status,'deActiveCamera')
        global deActive
        deActive=True;
        
def takePicture():
    BUTTON_PIN = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    previous_button_state = GPIO.HIGH
    camera =PiCamera()
    camera.resolution = (800,800)
    camera.rotation = 90
    camera.iso = 1600
    camera.framerate = 30
    camera.shutter_speed = 8000
    
    pictureSet=0
    global deActive
    deActive=False
    
    while True :
            if deActive==True or pictureSet>=2:
                print('break')
                break;
            
            sleep(0.01)
            button_state = GPIO.input(BUTTON_PIN)
            if button_state != previous_button_state:
                if previous_button_state == GPIO.HIGH:
                    print("preview")
                    camera.start_preview(alpha=200)
                previous_button_state = button_state
                if button_state == GPIO.HIGH:
                    
                    print("button has just been released")
                    pictureSet +=1
                    numberOfimage=pictureSet
                    
                    #take photo
                    for i in range(3):
                        sleep(1)
                        print("set",numberOfimage," takePhoto",i)
                        camera.capture("/home/pi/Desktop/image/image%s.jpg" %(str(numberOfimage)+"-"+str(i)) )
                    camera.stop_preview()
    
                    #send photo
                    dataDic={}
                    for i in range(3):
                        pic = open("/home/pi/Desktop/image/image{Set}-{num}.jpg".format(Set=str(numberOfimage),num=str(i)) ,'rb')
                        image_data = pic.read()
                        dataDic["image{num}".format(num=str(i))]=image_data
                    sio.emit('image', {"imageSide{Set}".format(Set=str(numberOfimage)): dataDic})
    camera.close()
    if deActive==False:
        sio.emit('sendstatus',False)

main(host,port)