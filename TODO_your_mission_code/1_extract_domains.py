from datetime import datetime
import json
import requests
import re
from time import sleep
from crayons import *

        
if __name__ == '__main__':
    print('This script extract every domain name contained into a web page and retrieves all domain\'s security information from Umbrella Investigate BackEnd')
    print()
    print('===================================================================================================================')
    print()
    print(yellow('This Script is bugged !!! You have to debug it !!!',bold=True))     
    print(yellow('Comment what is useless and uncomment what is needed',bold=True))     
    print() 
    #TODO MISSION : comment useless things and uncomment useful ones
    url=input("enter a HTTP domain a URL to check ( ex www.cars.com ) ( You can type Enter to read a file in disk ): ")
    url = url.replace('https://','')
    url = url.replace('HTTPS://','')
    url = url.replace('http://','')
    url = url.replace('HTTP://','')

    url='https://' + url
    html=requests.get(url).text
    
    #TODO MISSION : comment useless things and uncomment useful ones
    '''
    # Open a file on disk
    with open("page.html", "r") as file:
        html=file.read()
    print(html)
    '''
    links = re.findall('"((http|ftp)s?://.*?)"', html)
    domains =[]
    for link in links:
        #print (link[0])
        domain=link[0].replace("https://","")
        domain=domain.replace("http://","")
        domain=domain.split('/')
        if domain[0] not in domains:
            domain[0]=domain[0].replace("\\","")
            domains.append(domain[0])
    for domain in domains:
        print (domain)