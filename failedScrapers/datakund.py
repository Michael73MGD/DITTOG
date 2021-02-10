from datakund.datakund import *
obj=datakund()
youtube=obj.youtube()
youtube.open("video_url")
youtube.keypress('pagedown')
allcomments=[]
lastpagesource=youtube.get_page_source()
currentpagesource=''
while(True):
    if(lastpagesource==currentpagesource):
        break
    lastpagesource=currentpagesource
    response=youtube.video_comments(fields=['Comment'])
    for data in response['body']:
        allcomments.append(data)
    youtube.scroll()
    currentpagesource=youtube.get_page_source()
    
#https://youtube-api.datakund.com/en/latest/video_comments.html