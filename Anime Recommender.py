from re import *
from urllib.request import urlopen
from tkinter import *
from random import randint
pattern = 'Anime: (.*?)\"'
source = 'https://myanimelist.net/topanime.php'
read_source = urlopen(source) .read() .decode("UTF-8")
matches = findall(pattern, read_source)
print(matches[randint(0,50)])
