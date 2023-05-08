from datetime import datetime
import json
import requests

#base_url="https://investigate.api.umbrella.com"
base_url="http://localhost:4000"
#TODO  MISSION : enter here under your INVESTIGATE API Key
investigate_api_key = "INVESTIGATE_API_KEY"
#create header for authentication and set limit of sample return to 1
headers = {
'Authorization': 'Bearer ' + investigate_api_key,
'limit': '1'
}

def check_reputation(header,file):
    #TODO  MISSION : set the API path needed  to query for a single domain ( https://docs.umbrella.com/investigate-api/docs )
    # time for AlertTime and EventTime when domains are added to Umbrella
    time = datetime.now().isoformat()
        
    # loop through domains.txt file and append every domain to list, skip comments
    domain_list = []
    with open('domains.txt') as inputfile:
        for line in inputfile:
            if line[0] == "#" or line.strip() == "Site":
                pass
            else:
                domain_list.append(line.strip())

    fi = open("reputation.txt", "w")
    # loop through all domains
    for domain in domain_list:
        print(domain)
        # assemble the URI, show labels give readable output
        #TODO  MISSION : set the API path needed  to query for a single domain ( https://docs.umbrella.com/investigate-api/docs )        
        api_path = "/domains/???????/"
        get_url = f"{base_url}{api_path}{domain}"        
        # do GET request for the domain status and category
        request_get = requests.get(get_url, headers=headers)
        if(request_get.status_code == 200):
            # store categorization into the output variable
            output = request_get.json()
            resp2=json.dumps(output,sort_keys=True,indent=4, separators=(',', ': '))
            print(resp2)
            # FIRST let's retreive the domain status
            domain_output = output[domain] #we need this as the domain name in the json result is always changing
            domain_status = domain_output["status"] #a now we can retreive the status for the domain name
            # walk through different options of status
            if(domain_status == -1):
                print("SUCCESS: The domain %(domain)s is found MALICIOUS at %(time)s" % {'domain': domain, 'time': time})
                fi.write(domain+'; DANGEROUS ;'+time+';')
            elif(domain_status == 1):
                print("SUCCESS: The domain %(domain)s is found CLEAN at %(time)s" % {'domain': domain, 'time': time})
                fi.write(domain+'; CLEAN ;'+time+';')            
            else:
                print("SUCCESS: The domain %(domain)s is found UNDEFINED / RISKY at %(time)s" % {'domain': domain, 'time': time})
                fi.write(domain+'; UNKNOWN;'+time+';')
            fi.write('\r\n')

if __name__ == '__main__':
    print('This script GET from the Umbrella Investigate BackEnd, the reputation of all domains contained into the domains.txt file')
    print('Search in this Script for all [ #TODO  MISSION : ] statements and add missing information')
    print()
    print('==================================================================================================================================')
    print() 
    check_reputation(headers,'domains.txt')
    