from datetime import datetime
import json
import requests


# copy paste API key from investigate within the quotes
#base_url="https://investigate.api.umbrella.com"
base_url="http://localhost:4000"
#TODO  MISSION : enter here under your INVESTIGATE API Key
investigate_api_key = "INVESTIGATE_API_KEY"
#create header for authentication and set limit of sample return to 1
headers = {
'Authorization': 'Bearer ' + investigate_api_key,
'limit': '1'
}

def retrieve_categorie(header):
    #TODO  MISSION : set the API path needed  to query for a single domain ( https://docs.umbrella.com/investigate-api/docs )        
    api_path = "/domains/???????/"
    get_url = f"{base_url}{api_path}"
    # do GET request for the domain status and category
    request_get = requests.get(get_url, headers=headers)
    if(request_get.status_code == 200):
        # store all categories into a variable named output
        output = request_get.json() 
        return output

if __name__ == '__main__':
    print('This script GET from the Umbrella Investigate BackEnd, All Categories and their indexex')
    print('Search in this Script for all [ #TODO  MISSION : ] statements and add missing information')
    print()
    print('==================================================================================================================================')
    print() 
    categories=retrieve_categorie(headers)
    print(categories)
    '''
    for cle,valeur in categories.items():
        print (cle+' '+ valeur)
    '''
    