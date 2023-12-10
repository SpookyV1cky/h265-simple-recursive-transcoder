import os
import ffmpeg
from os.path import join, getsize
from util.db import *
import time

VIDEO_CODEC = 'hevc_nvenc' #this is for nvidia, for CPU u can specify libx265

def transcod(video, out, new_bitrate, audio_codec, audio_bitrate):
    
    (
    ffmpeg
    .input(video)
    .output(out, **{'b:v': new_bitrate, 'codec:v':VIDEO_CODEC, 'preset': 'slow', 'b:a':audio_bitrate, 'codec:a': audio_codec})
    .run()
    )
    print("[ OK ]")


def process(tasklist):

    for task in tasklist:
        if(task['status'] == False):
            print("transcoding " + task['name'])
            new_bitrate = int(float(task['bit_rate']) * .60) #60%
            try:
                transcod(task['path'], task['out'], new_bitrate, task['audio_codec'], task['audio_bitrate'])
                task['status'] = True
            except:
                time.sleep(0.5)
                os.remove(task['out'])
                print(' \n UnU Bye Bye </3 ')
                break
    db_save(tasklist)