import requests
import pprint
import json

response = requests.get('http://onesearch.cuny.edu/PrimoWebServices'
                        '/xservice/search/brief?'
			'&institution=KB'
			'&query=any,contains,cuny'
			'&loc=adaptor,primo_central_multiple_fe'
			'&json=true')

output = str(response.text.encode('UTF-8'))


with open('myfile.txt', 'w') as file:
    file.write(output)
