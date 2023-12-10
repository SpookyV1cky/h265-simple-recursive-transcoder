import os
import ffmpeg
import sys
from os.path import join, getsize
from util.db import *
from util.process import *
from util.video_finder import find_something


def main():
    
    tasklist = db_load()
    
    if(tasklist):
        
        if(input('continue from the last session?(Y/N)').lower() =='y' ):
            process(tasklist)
        else:
            tasklist = find_something()
            process(tasklist)
            
    else:
        tasklist = find_something()
        process(tasklist)
main()

