import time
import csv
import random
from youtube_channel_videos_scraper import *
youtube.open("https://www.youtube.com/c/DougDeMuro/videos")

for i in range(0,30):
    youtube.keypress("pagedown")
    time.sleep(0.25)
time.sleep(1)
get_videos = youtube.channel_videos()
videos = get_videos['body']
#videos=[{"Title": "Title", "Video_Link": "Video_Link"}]
video_count = len(videos)
filename = "videos.csv"
with open(filename, 'a', encoding="utf-8", newline='') as csvfile:  
    csvwriter = csv.writer(csvfile)   
    #csvwriter.writerow(testComment)
    for i in range(0,video_count):
        title = videos[i]['Title']
        link = videos[i]['Video_Link']
        line = [title,link]
        csvwriter.writerow(line)
        #print(videos[i]['Title']+" - " + videos[i]['Video_Link'])