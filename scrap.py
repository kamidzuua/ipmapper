import sys
import time
import requests
from bs4 import BeautifulSoup
from termcolor import colored

page = open('ru - bgp.he.net.html')
soup = BeautifulSoup(page,'html.parser')
listFile = open("list.txt","a")

allRows = soup.find_all('tr')
counter = 0
for row in allRows:
    ip = row.find_next('a').get_text()
    ipSplit = ip.split('.')
    if ipSplit[0].isalpha():
        continue
    if len(ipSplit[0]) > 3:
        continue
    flag = row.find_next('img')['title']
    if flag != "Russian Federation":
        print(colored(flag+' '+ip,'red'))
    else:
        print(colored(flag+' '+ip,'green'))
        listFile.write('"'+ip+'" ')

listFile.close()