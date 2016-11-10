# import the libraries that you need
import requests
import json

# make a GET request to the OneSearch X-Service API
response = requests.get('http://onesearch.cuny.edu/PrimoWebServices'
                        '/xservice/search/brief?'
			'&institution=KB'
			'&query=any,contains,cuny'
			'&loc=adaptor,primo_central_multiple_fe'
			'&json=true')

# take the JSON from the response, and store it in a variable called alldata 
alldata = response.json()
output = alldata['SEGMENTS']['JAGROOT']['RESULT']['FACETLIST']['FACET'][0]['FACET_VALUES']
print(output)

# open a file called myfile.txt and write the output to that file
with open('mydata.txt', 'w') as file:
   json.dump(output, file) 
