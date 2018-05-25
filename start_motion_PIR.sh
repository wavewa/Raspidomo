#!/bin/bash


#nohup /home/wave/motion-mmal/motion-mmal -n -c /home/wavr/motion-mmal/cmmal.conf 1>/dev/null 2>&1 </dev/null &
 
exec /home/pi/script/videosorveglianza/motion_PIR.py 1>/dev/null 2>&1 </dev/null &
