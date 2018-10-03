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

subfolder = "\ANIMEVIDS"
videos = os.listdir(subfolder)

# ENTER FOLDER ON SYSTEM WITH AUDIO CLIPS YOU WANT TO USE.
mp3dir = "\SONGS"
mp3s = os.listdir(mp3dir)

r = random.randint(0, len(mp3s) - 1)
y = os.path.join(mp3dir, mp3s[r])
song = AudioFileClip(y)
duration = song.duration

# DEFINE IN AND OUT TIME LIMITS IN SECONDS FOR THE VIDEO. I CHOOSE 120 START TO SKIP INTRO.
I = 200
O = 1080

clips = []

num_clips = 0
while(num_clips<150):
    
    outputname = str(random.randint(1000,10000))+".mp4"
    
    x = random.randint(0, len(videos) - 1)
    video = os.path.join(subfolder, videos[x])
    n = random.randint(2, 4)
    l = random.randint(I, O)
    clip = VideoFileClip(video, audio=False).subclip(l, l+n)
    clips.append(clip)
    num_clips=num_clips + 1
    
# FINAL ASSEMBLY - COMPOSE WILL PREVENT GLITCHES WHEN USING ANIME WITH DIFFERENT RESOLUTIONS.
    
final = mp.concatenate_videoclips(clips,method="compose").subclip(0,duration).set_audio(song)
final.write_videofile(outputname,preset='ultrafast',threads=4,progress_bar = False,)
