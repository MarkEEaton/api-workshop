# import the libraries that you need
import requests
import json

# make a GET request to the OneSearch X-Service API
response = requests.get('http://onesearch.cuny.edu/PrimoWebServices'
                        '/xservice/search/brief?'
                        '&institution=KB'
                        '&query=any,contains,obama'
                        '&query=facet_rtype,exact,books'
                        '&loc=adaptor,primo_central_multiple_fe'
                        '&loc=local,scope:(KB,AL,CUNY_BEPRESS)'
                        '&json=true')

# take the json data from the response
output = response.json()

# open a file called myfile.txt and write the output to that file
with open('myfile.txt', 'w') as f:
    json.dump(output, f)
