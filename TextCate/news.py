import keyboard as keyboard
from bs4 import BeautifulSoup
import requests
import os

source = requests.get('https://www.prothomalo.com/bangladesh/article').text

soup = BeautifulSoup(source, 'lxml')

for posts in soup.find_all('div', class_='info has_ai'):
    headline = posts.find('span', class_='title').text





    print(headline)

    #fileName = input("Give a file name: ") + ".txt"
    #scrappedFile = open(fileName, 'w')
    #scrappedFile.write(str(headline))
    #scrappedFile.close()

    #os.startfile(fileName)
