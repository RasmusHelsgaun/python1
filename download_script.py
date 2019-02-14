import os
import urllib.request as req
from urllib.parse import urlparse
import sys

urlList = sys.argv[2:]
to = sys.argv[1]
def download(urlList, to):
    for url in urlList:
        fileName = url.split("/")[-1]
        req.urlretrieve(url,to + fileName)
        print(fileName + " has been created")
download(urlList, to)