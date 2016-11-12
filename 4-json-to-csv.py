# import the libraries that you need
import requests
import json
import csv

# make a GET request to the OneSearch X-Service API
response = requests.get('http://onesearch.cuny.edu/PrimoWebServices'
                        '/xservice/search/brief?'
			'&institution=KB'
			'&query=any,contains,cuny'
			'&loc=adaptor,primo_central_multiple_fe'
			'&json=true')

# take the JSON from the response
# and store it in a variable called alldata 
alldata = response.json()

# drill down into a smaller subset of the json 
# and print this smaller bit of json 
someoutput = alldata['SEGMENTS']['JAGROOT']['RESULT']['FACETLIST']['FACET'][7]['FACET_VALUES']

# open a file called mydata.txt and write the output to that file
with csv.writer(open('mycsv.csv', 'wb+')) as file:
    for x in somedata:
        file.writerow([somedata['@KEY'],
                      [somedata['@VALUE']])
