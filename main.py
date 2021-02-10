#Reads videos.csv and updates data.csv by calling DITTOG.py
import csv
import random
import time
import sys
import subprocess
from youtube_comment_scraper import *

videos = 'videos.csv'
with open(videos, 'r', encoding="utf-8", newline='') as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=',')  
    line_count = 0
    for row in csvreader:            
        line_count += 1
        url = row[1]
        title = row[0]
        print("Opening " + url)
        print("Title is " + title)
        youtube.open(url)
        time.sleep(2)
        youtube.keypress("pagedown")
        time.sleep(2)
        for i in range(0,100):      #Enough for about 500 comments
            youtube.keypress("pagedown")
            time.sleep(0.3)
        time.sleep(1)
        response=youtube.video_comments()
        data=response['body']
        comment_count = len(data)
        print("Downloaded "+str(comment_count)+" comments.")
        time.sleep(3)
        filename = "data.csv"
        with open(filename, 'a', encoding="utf-8", newline='') as csvfile2:  
            csvwriter = csv.writer(csvfile2)   
            for i in range(0,comment_count):
                print("Testing comment #"+str(i))
                comment = data[i]["Comment"]
                if "Doug is the" in comment or "Doug's the" in comment or "doug is the" in comment or "doug's the" in comment or "Doug the" in comment or "doug the" in comment or "the kind of guy" in comment or "the type of guy" in comment or "the kinda guy" in comment:
                    user = data[i]["user"]
                    likes = data[i]["Likes"]
                    line = [comment,user,likes,title]
                    csvwriter.writerow(line)