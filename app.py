import os
import ffmpeg
import sys
from os.path import join, getsize

VIDEO_CODEC = 'hevc_nvenc' #this is for nvidia, for CPU u can specify libx265

def transcod(video, out, new_bitrate, audio_codec, audio_bitrate):
    
    (
    ffmpeg
    .input(video)
    .output(out, **{'b:v': new_bitrate, 'codec:v':VIDEO_CODEC, 'preset': 'slow', 'b:a':audio_bitrate, 'codec:a': audio_codec})
    .run()
    )
    print("[ OK ]")

def main():

    rootfolder = sys.argv[1]
    for root, dirs, files in os.walk(rootfolder):
        
        for name in files:
                
                if(name.split('.').pop() == 'mp4'):
                    video = os.path.join(root, name)
                    
                    metadata = ffmpeg.probe(video)
                    codec = metadata['streams'][0]['codec_name']
                    
                    bit_rate = metadata['streams'][0]['bit_rate']
                    new_bitrate = int(float(bit_rate) * .60) #60%
                
                    audio_codec = metadata['streams'][1]['codec_name']
                    audio_bitrate = metadata['streams'][1]['bit_rate']

                    if(codec == 'h264'):
                        out = os.path.join(root, "h265_" + name)
                        print("transcoding " + video)
                        transcod(video, out, new_bitrate, audio_codec, audio_bitrate)
                    else:
                        print("ignoring " + name + " (NOT H.264)") 

main()

