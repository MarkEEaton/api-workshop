# import the libraries that you need
import requests
import csv

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
somedata = alldata['SEGMENTS']['JAGROOT']['RESULT']['FACETLIST']['FACET']\
                  [7]['FACET_VALUES']
print(somedata)

# open a file called mycsv.csv, then loop through the data
# and write to that file
with open('mycsv.csv', 'wb') as f:
    writer = csv.writer(f)
    for x in somedata:
        writer.writerow([x['@KEY'], x['@VALUE']])
