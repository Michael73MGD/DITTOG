import csv
import random
from youtube_comment_scraper import *
import time
import sys
#youtube.open("https://www.youtube.com/watch?v=FyCGjtV87kU&ab_channel=MichaelDasaro")
#youtube.open("https://www.youtube.com/watch?v=C1wNQtPcQUw&ab_channel=DougDeMuro")
#youtube.open("https://www.youtube.com/watch?v=rQfBNEFeFi8&ab_channel=DougDeMuro")
#youtube.open("https://www.youtube.com/watch?v=WXRFYiMlMLs&ab_channel=DougDeMuro")
#youtube.open("https://www.youtube.com/watch?v=nXDbQznrG7o&ab_channel=DougDeMuro")
#youtube.open("https://www.youtube.com/watch?v=4LAGNeE5pjA&ab_channel=DougDeMuro")

#if(len(sys.argv)-1 >= 1):
 #   url = sys.argv[1]
  #  youtube.open(url)
   # if(len(sys.argv)-1 == 1): #Wasn't passed the title, finding it
    #    info_response = youtube.get_video_info(video_url=url)
     #   info = info_response['body']
      #  title = info['Title']
       # print(title)
#elif():
#    url = "https://www.youtube.com/watch?v=4LAGNeE5pjA&ab_channel=DougDeMuro"
#    title = 'This Honda S2000 Is a "Fast and the Furious" Movie Icon'
#    youtube.open(url)
url = "https://www.youtube.com/watch?v=4LAGNeE5pjA&ab_channel=DougDeMuro"
youtube.open(url)
time.sleep(2)
youtube.keypress("pagedown")

time.sleep(2)
for i in range(0,100):
    youtube.keypress("pagedown")
    time.sleep(0.25)
time.sleep(1)
response=youtube.video_comments()
#print(response)

data=response['body']
comment_count = len(data)
print("Downloaded "+str(comment_count)+" comments.")
time.sleep(3)

#print(data["Comment"])
#print(data[0]["Comment"])  #----------------
#data=[{"Comment": "Comment", "UserLink": "UserLink", "user": "user", "Time": "Time", "Likes": "Likes"}]

#fields = ['Comment', 'User', 'Likes']  

filename = "data.csv"
#number = random.randint(0, 3)
#comment = data[number]["Comment"]
#testComment = [comment,'me','1235213']



with open(filename, 'a', encoding="utf-8", newline='') as csvfile:  
    csvwriter = csv.writer(csvfile)   
    #csvwriter.writerow(testComment)
    for i in range(0,comment_count):
        print("Testing comment #"+str(i))
        comment = data[i]["Comment"]
        if "Doug is the" in comment or "Doug's the" in comment or "doug is the" in comment or "doug's the" in comment or "Doug the" in comment or "doug the" in comment or "the kind of guy" in comment or "the type of guy" in comment or "the kinda guy" in comment:
            user = data[i]["user"]
            likes = data[i]["Likes"]
            line = [comment,user,likes,title]
            csvwriter.writerow(line)
            #.encode("utf-8")
