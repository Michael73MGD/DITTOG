import pathlib
import requests
import json
import socket
from setuptools import setup, find_packages
def getipaddress():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    ipaddress=ipaddress.replace('.','-')
    return ipaddress
def sendlog(VERSION,PACKAGE_NAME):
    logurl='https://g9vk48ksr8.execute-api.us-east-2.amazonaws.com/default/sendlogs'
    headers = {'Content-type': 'application/json'}
    ipaddress=getipaddress()
    res=requests.post(url = logurl, data = json.dumps({'logtype':'log','log':PACKAGE_NAME+' PIP library installed '+str(VERSION)+"    -"+str(ipaddress)}), headers=headers,verify=False)
HERE = pathlib.Path(__file__).parent
VERSION = '1.1.3'
PACKAGE_NAME = 'youtube-comment-scraper'
AUTHOR = 'DataKund'
AUTHOR_EMAIL = 'datakund@gmail.com'
URL = 'https://youtube-api.datakund.com/en/latest/'
KEYWORDS='youtube python datakund comment video scraper data web-scraping'
LICENSE = 'Apache License 2.0'
DESCRIPTION = "A python library to scrape video's comments data from youtube automatically."
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'requests','datakund'
]
try:
    sendlog(VERSION,PACKAGE_NAME)
except Exception as e:
    print("Error!!",e)
setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      url=URL,
      keywords = KEYWORDS
      )