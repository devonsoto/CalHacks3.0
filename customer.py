# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

customerId = '58274dfb360f81f104547a74'
apiKey = '18f3a2575d68ead99755eb8f54bf9d66'

url = 'http://api.reimaginebanking.com/customers?key=18f3a2575d68ead99755eb8f54bf9d66'.format(customerId,apiKey)
payload = {
  "first_name": "string",
  "last_name": "string",
  "address": {
    "street_number": "string",
    "street_name": "string",
    "city": "string",
    "state": "Co",
    "zip": "80601"
  }
}
# Create a customer
response = requests.post(
	url,
	data=json.dumps(payload), 
	headers={'content-type':'application/json'},
    )
if response.status_code == 201:
	print('customer created')
