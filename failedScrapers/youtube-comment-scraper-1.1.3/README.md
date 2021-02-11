Youtube-Comment-Scraper is a python library to fetch video comments on youtube using browser automation. 
It currently runs only on windows.

### Example
In this example we first import library, then we will open the video and load its comments and then fetch them.
```sh
from youtube_comment_scraper import *
youtube.open("video url")
youtube.keypress("pagedown")
response=youtube.video_comments()
data=response['body']
#data=[{"Comment": "Comment", "UserLink": "UserLink", "user": "user", "Time": "Time", "Likes": "Likes"}]
```

This module depends on the following python modules
* [requests](https://pypi.org/project/requests/)
* [datakund](https://pypi.org/project/datakund/)

#### DataKund
[datakund](https://pypi.org/project/datakund/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which video will be opend and comments will be fetched.

Complete documentation for YouTube Automation available [here](https://youtube-api.datakund.com/en/latest/)

### Installation

```sh
pip install youtube-comment-scraper
```

### Import
```sh
from youtube_comment_scraper import *
```

### Open video link
```sh
youtube.open("video link")
```

### Load comments
```sh
youtube.keypress("pagedown")
```

### Get comments
```sh
response=youtube.video_comments()
data=response['body']
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

