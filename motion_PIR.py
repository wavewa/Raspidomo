#!/usr/bin/env python

from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import subprocess
import shlex
import os
os.chdir('./registrazioni') # Provide the path here
#print os.getcwd(); # Prints the working directory

camera = PiCamera()
pir = MotionSensor(7)

try:
 while True:
   #try:
    pir.wait_for_motion()
    filename =  datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
#    filename = './registrazioni' + datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    #filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.mjpeg")
    #camera.resolution = (640, 360)
    #camera.framerate = 24
    #subprocess.Popen(["bash", "../send1"])

    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_recording()
   # camera.close()
    # execfile('/home/wave/send') 
    #subprocess.call(shlex.split('/home/wave/send param1 param2'))
    # print  subprocess.check_call(["ls", "-l ../"])
    #subprocess.Popen(["bash", "../send1"])
    subprocess.call('./sendmail')
except KeyboardInterrupt:
    pass
finally:
    camera.close()
