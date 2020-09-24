from datetime import datetime
import json
import requests
import re
from time import sleep

if __name__ == '__main__':
    print('This script test the Umbrella Investigate Simulator')
    print()
    print('==================================================================================================================================')
    print()    
    # cleanup
    url = "http://localhost:4000/test"
    html=requests.get(url).text
    print(html)
