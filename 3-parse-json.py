# import the libraries that you need
import requests
import json

# make a GET request to the OneSearch X-Service API
response = requests.get('http://onesearch.cuny.edu/PrimoWebServices'
                        '/xservice/search/brief?'
                        '&institution=KB'
                        '&query=any,contains,cuny'
                        '&query=facet_rtype,exact,books'
                        '&loc=adaptor,primo_central_multiple_fe'
                        '&loc=local,scope:(KB,AL,CUNY_BEPRESS)'
                        '&json=true')

# take the JSON from the response
# and store it in a variable called alldata
alldata = response.json()

# drill down into a smaller subset of the json
# and print this smaller bit of json
output = alldata['SEGMENTS']['JAGROOT']['RESULT']['FACETLIST']\
                ['FACET'][7]['FACET_VALUES']
print(output)

# open a file called mydata.txt and write the output to that file
with open('mydata.txt', 'w') as f:
    json.dump(output, f)
