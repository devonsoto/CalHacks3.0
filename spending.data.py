import requests
import json
from pprint import pprint

def withdraw( amount ):
    customerId = '58282f94360f81f10454bd2a'
    apiKey = '18f3a2575d68ead99755eb8f54bf9d66'

    url = 'http://api.reimaginebanking.com/accounts/58283089360f81f10454bd2f/purchases?key=18f3a2575d68ead99755eb8f54bf9d66'.format(customerId,apiKey)
    payload = {
    "merchant_id": "57cf75cea73e494d8675ec49",
    "medium": "balance",
    "purchase_date": "2016-11-12",
    "amount": amount,
    "description": "string"
    }
    # Create a customer
    response = requests.post(
	   url,
	   data=json.dumps(payload),
	   headers={'content-type':'application/json'},
        )

def deposit( amount ):
    customerId = '58282f94360f81f10454bd2a'
    apiKey = '18f3a2575d68ead99755eb8f54bf9d66'

    url = 'http://api.reimaginebanking.com/accounts/58283089360f81f10454bd2f/deposits?key=18f3a2575d68ead99755eb8f54bf9d66'.format(customerId,apiKey)
    payload = {
    "medium": "balance",
    "transaction_date": "2016",
    "amount": amount,
    "description": "initial balance"
    }
    # Create a customer
    response = requests.post(
	   url,
	   data=json.dumps(payload),
	   headers={'content-type':'application/json'},
       )
    data1 = response.json();
    return data1;

def getAccount( accNum ):
    customerId = '58282f94360f81f10454bd2a'
    apiKey = '18f3a2575d68ead99755eb8f54bf9d66'

    url = 'http://api.reimaginebanking.com/accounts/58283089360f81f10454bd2f?key=18f3a2575d68ead99755eb8f54bf9d66'.format(customerId,apiKey)
    payload = {
    "_id": accNum
    }
    # Create a customer
    response = requests.get(
	   url,
	   data=json.dumps(payload),
	   headers={'content-type':'application/json'},
        )
    data1 = response.json();
    return data1;

aNum = "58283089360f81f10454bd2f";
tBalance = getAccount(aNum);
zero = tBalance['balance'];
withdraw(zero);
inBal = 4000;
deposit(inBal);
list = [50, 400, 1200];

for i in range(0,3):
    amount = list[i];
    withdraw(amount);

fAData = getAccount(aNum);
fBal = fAData['balance'];
print(fBal);
