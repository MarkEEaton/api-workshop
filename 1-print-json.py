# import the libraries that you need
import requests
import pprint


# make a GET request to the OneSearch X-Service API
response = requests.get('http://onesearch.cuny.edu/PrimoWebServices'
                        '/xservice/search/brief?'
                        '&institution=KB'
                        '&query=any,contains,obama'
                        '&query=facet_rtype,exact,books'
                        '&loc=adaptor,primo_central_multiple_fe'
                        '&loc=local,scope:(KB,AL,CUNY_BEPRESS)'
                        '&json=true')

# take the JSON from the response and store it in a variable called output
output = response.json()

# write the output to the screen
pprint.pprint(output)
