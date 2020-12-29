import os
import shutil
import time

DownloadsDir = ''
ImageFolder = ''

while True:
    time.sleep(.3)
    Downloadslst = os.listdir(DownloadsDir) 
    for files in Downloadslst:
        if files.endswith(('.png','.jpg')):
            shutil.move(DownloadsDir + '/' + files, ImageFolder)
            print('File moved succefully.')
