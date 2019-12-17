'''
  API requests in python using the requests lib. 

  APIs tested: 
    - Palo Alto Open Data 


'''


import requests as req 
import json


PALO_ALTO_KEY = 'f8e23d20b6e68d597d56cb0da9115e9779c4631b'

# 'http://paloalto.cloudapi.junar.com/api/v2/datastreams/GENER-RESID-WATER-SERVI-UTILI/data.json/?auth_key=YOUR_API_KEY'

palo_alto = req.get('http://paloalto.cloudapi.junar.com/api/v2/datasets/PALO-ALTO-CITY-LIBRA-COLLE/?auth_key=f8e23d20b6e68d597d56cb0da9115e9779c4631b')
print(palo_alto.content)
# print(json.dumps(json_data, indent=2))

# with open('palo_alto_explore1.json', 'w') as file: 
#   file.write(json.dumps(json_data, indent=2))