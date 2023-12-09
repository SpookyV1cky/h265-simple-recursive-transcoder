import os
import ffmpeg
import sys
import colorama
from colorama import Back, Fore, Style
from os.path import join, getsize

def main():
    colorama.init(autoreset = True)

    rootfolder = sys.argv[1]
    for root, dirs, files in os.walk(rootfolder):
        
        for name in files:
                
                if(name.split('.').pop() == 'mp4'):
                    video = os.path.join(root, name)
                    
                    metadata = ffmpeg.probe(video)
                    codec = metadata['streams'][0]['codec_name']
                    
                    if(codec == 'h264'):
                        print(Fore.RED + "Deleting " + name + "...")
                        os.remove(video)
                    else:
                        print(Fore.GREEN + "ignoring " + name + " (NOT H.264)") 
    
    print(Fore.GREEN + "[ See you later :3 ]")
main()