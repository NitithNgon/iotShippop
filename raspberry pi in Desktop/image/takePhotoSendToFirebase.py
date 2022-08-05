from picamera import PiCamera
from time import sleep
import requests
from pprint import pprint
url = "https://us-central1-imbedded-system.cloudfunctions.net/uploadFile"

f = open("num", "r")
numberOfimage=int(f.read())
f.close()
camera =PiCamera()
camera.resolution = (800,800)
camera.rotation = 90
# camera.iso = 1600
camera.framerate = 30
camera.shutter_speed = 8000

camera.start_preview(alpha=250)
sleep(1)

#take photo
for i in range(3):
    sleep(1)
    print("set",numberOfimage," takePhoto",i)
    camera.capture("/home/pi/Desktop/image/image%s.jpg" %(str(numberOfimage)+"-"+str(i)) )
camera.stop_preview()

#send photo firebase
for i in range(3):
    payload={}
    files=[('file',("image{Set}-{num}.jpg".format(Set=str(numberOfimage),num=str(i)) ,open("/home/pi/Desktop/image/image{Set}-{num}.jpg".format(Set=str(numberOfimage),num=str(i)) ,'rb'),'image/jpeg'  ))]
    headers = {}
    #response = requests.request("POST", url, headers=headers, data=payload, files=files)
    #pprint(response.text)

f = open("num", "w")
f.write(str(int(numberOfimage)+int(1)))
f.close()
