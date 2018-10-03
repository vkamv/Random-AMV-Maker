import random
import time
import subprocess
import os
import sys
from multiprocessing import Process
from moviepy.editor import *
from moviepy.editor import VideoFileClip
import moviepy.editor as mp

# ENTER FOLDER ON SYSTEM WITH VIDEO CLIPS YOU WANT TO USE.

subfolder = "X:\AnimeClips"
videos = os.listdir(subfolder)

# ENTER FOLDER ON SYSTEM WITH AUDIO CLIPS YOU WANT TO USE.
mp3dir = "Z:\MP3FILES"
mp3s = os.listdir(mp3dir)

r = random.randint(0, len(mp3s) - 1)
y = os.path.join(mp3dir, mp3s[r])
print(y)
song = AudioFileClip(y)

# MAKES SURE THAT FINAL DURATION IS LIMITED TO SONG LENGTH.
duration = song.duration

# DEFINE IN AND OUT TIME LIMITS IN SECONDS FOR THE VIDEO. I CHOOSE 200 START TO SKIP INTRO. 1080 IS BASED ON 18 MINUTES X 60 SECS.
I = 200
O = 1080

clips = []

print ("CREATING RANDOM SUBCLIPS")

num_clips = 0
while(num_clips<150):
    
    x = random.randint(0, len(videos) - 1)
    video = os.path.join(subfolder, videos[x])
    n = random.randint(2, 4)
    l = random.randint(I, O)
    clip = VideoFileClip(video, audio=False).subclip(l, l+n)
    clips.append(clip)
    num_clips=num_clips + 1

#RANDOM GENERATED OUTPUT NAME. GOOD FOR WHEN YOUR MAKING A BATCH OF RANDOM FINAL VIDEOS. CHANGE EXTENSION TO WHICHEVER YOU PLEASE

outputname = str(random.randint(1000,10000))+".mp4"

# FINAL ASSEMBLY - COMPOSE WILL PREVENT GLITCHES WHEN USING ANIME WITH DIFFERENT RESOLUTIONS.
print ("CONCATING CLIPS")
final = mp.concatenate_videoclips(clips,method="compose").subclip(0,duration).set_audio(song)
print ("CREATING FINAL VIDEO")
final.write_videofile(outputname,preset='ultrafast',threads=4,progress_bar = False,)
