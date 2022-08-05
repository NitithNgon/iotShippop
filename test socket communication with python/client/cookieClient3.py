import socket
from time import time

host = '192.168.43.192'
port = 5560

def setupSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def sendPic(s, filePath, picName):
    print(filePath)
    pic = open(filePath, 'rb')
    chunk = pic.read(1024)
    filePathServer = "C:\\Users\\User PC\\Desktop\\shippop\\Socket Communication\\receiveImage\\"+picName
    s.send(str.encode("STORE " + filePathServer))
    t = time()
    while chunk:
        print("Sending Picture")
        s.send(chunk)
        chunk = pic.read(1024)
    pic.close()
    print("Done sending")
    print("Elapsed time = " + str(time() - t) + 's')
    s.close()
    return "Done sending"

def backup(filePath,picName):
    s = setupSocket()
    response = sendPic(s, filePath, picName)
    return response
