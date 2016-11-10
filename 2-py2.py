# import the libraries that you need
import requests

# make a GET request to the OneSearch X-Service API
response = requests.get('http://onesearch.cuny.edu/PrimoWebServices'
                        '/xservice/search/brief?'
			'&institution=KB'
			'&query=any,contains,cuny'
			'&loc=adaptor,primo_central_multiple_fe'
			'&json=true')

# take the JSON from the response, turn it into a string
# and store it in a variable called output
# you need to turn it into a string because a text file can't handle
# a JSON data structure
output = str(response.json())

# open a file called myfile.txt and write the output to that file
with open('myfile.txt', 'w') as file:
    file.write(output)
