from youtube_comment_scraper import *
youtube.open("https://www.youtube.com/watch?v=FyCGjtV87kU&ab_channel=MichaelDasaro")
youtube.keypress("pagedown")
response=youtube.video_comments()
data=response['body']
print(data)
#data=[{"Comment": "Comment", "UserLink": "UserLink", "user": "user", "Time": "Time", "Likes": "Likes"}]