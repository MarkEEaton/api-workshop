# import the libraries that you need
import requests

# make a GET request to the OneSearch X-Service API
response = requests.get('http://onesearch.cuny.edu/PrimoWebServices'
                        '/xservice/search/brief?'
			'&institution=KB'
			'&query=any,contains,cuny'
			'&loc=adaptor,primo_central_multiple_fe'
			'&json=true')

# take the JSON from the response, and store it in a variable called alldata 
alldata = response.json()
data = alldata['SEGMENTS']['JAGROOT']['RESULT']['FACETLIST']['FACET']
print(data)

# open a file called myfile.txt and write the output to that file
with open('mydata.txt', 'w') as file:
    file.write(output)
