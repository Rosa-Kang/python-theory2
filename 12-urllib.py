import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
  print(line.decode().strip())

#Scraping Web Pages
#What Python library is used for parsing HTML documents and extracting data from HTML documents? BeautifulSoup : parsing HTML
# To run the Beautiful Soup library, you can install BeautifulSoup from
# https://pypi.python.org/pypi/beautifylsoup4 or
# http://www.py4e.com/code3/bs4.zip unzip it in the same directory as this file.

#Python makes the complex simple
