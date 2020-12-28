import os
import shutil
import time

DownloadsDir = 'C:/Users/Alex/Downloads/'
ImageFolder = 'C:/Users/Alex/Desktop/edits and images/test'

while True:
    time.sleep(.3)
    Downloadslst = os.listdir(DownloadsDir) 
    for files in Downloadslst:
        if files.endswith(('.png','.jpg')):
            shutil.move(DownloadsDir + files, ImageFolder)
            print('File moved succefully.')
