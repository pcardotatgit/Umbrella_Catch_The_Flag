from datetime import datetime
from time import sleep
import json
import requests

#base_url="https://investigate.api.umbrella.com"
base_url="http://localhost:4000"
investigate_api_key = "#TODO  MISSION : enter here under your INVESTIGATE API Key"
#create header for authentication and set limit of sample return to 1
headers = {
'Authorization': 'Bearer ' + investigate_api_key,
'limit': '1'
}

def security_details(headers,domain):	
    # Third let's retrieve security values for this domain
    api_path = "/??????/?????/"  #TODO MISSION : Search an API_PATH with   name   and  Security...
    get_url = f"{base_url}{api_path}{domain}" 
    print(get_url)    
    request_get = requests.get(get_url, headers=headers)
    output = request_get.json()
    resp2=json.dumps(output,sort_keys=True,indent=4, separators=(',', ': '))
    print(resp2)	

if __name__ == '__main__':   
	security_details(headers,'#TODO MISSION : ENTER THE MALICIOUS DOMAIN NAME')
	