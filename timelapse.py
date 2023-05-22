from picamera import PiCamera
from os import system
import datetime
from time import sleep
import os

dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
new_dir_name = datetimeformat
current_directory = os.path.dirname(os.path.abspath(__file__))
create_directory = current_directory + '/' + new_dir_name

if(not (os.path.exists(create_directory))):
    os.mkdir(create_directory)

tlminutes = 2880 #set this to the number of minutes you wish to run your timelapse camera
secondsinterval = 1 #number of seconds delay between each photo taken
fps = 1 #frames per second timelapse video
numphotos = int((tlminutes*60)/secondsinterval) #number of photos to take
print("number of photos to take = ", numphotos)

print("RPi started taking photos for your timelapse at: " + datetimeformat)

camera = PiCamera()
camera.resolution = (1024, 768)

#system('rm /home/pi/usbmem/timelaps/photos/*.jpg') #delete all photos in the Pictures folder before timelapse start

for i in range(numphotos):
    camera.capture(create_directory + '/image{0:06d}.jpg'.format(i))
    sleep(secondsinterval)
print("Done taking photos.")
#print("Please standby as your timelapse video is created.")

#system('ffmpeg -r {} -f image2 -s 1024x768 -nostats -loglevel 0 -pattern_type glob -i "{}/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/{}.mp4'.format(fps, create_directory, datetimeformat))
#system('rm /home/pi/Pictures/*.jpg')
#print('Timelapse video is complete. Video saved as /home/pi/Videos/{}.mp4'.format(datetimeformat))

