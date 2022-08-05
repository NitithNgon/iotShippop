import picamera
from datetime import datetime
from cookieClient3 import backup

picPath = "/home/pi/Desktop/cookie/images/"

def captureImage(currentTime, picPath):
    # Generate the picture's name
    picName = currentTime.strftime("%Y.%m.%d-%H%M%S") + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(picPath + picName)
    print("We have taken a picture.")
    return picName

def getTime():
    # Fetch the current time
    currentTime = datetime.now()
    return currentTime

while True:
    currentTime = getTime()
    picName = captureImage(currentTime, picPath)
    print("Took a picture")
    completePath = picPath + picName
    print(completePath)
    backup(completePath,picName)
    print("Everything should be backed up now.")
    break

        
