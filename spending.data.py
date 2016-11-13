import requests
import json
from pprint import pprint

def withdraw( amount, debt ):
    amount = amount - debt;
    return amount;

def creAccount( cusNum, bal ):
    customerId = cusNum
    apiKey = '18f3a2575d68ead99755eb8f54bf9d66'

    url = 'http://api.reimaginebanking.com/customers/58282f94360f81f10454bd2a/accounts?key=18f3a2575d68ead99755eb8f54bf9d66'.format(customerId,apiKey)
    payload = {
    "type": "Checking",
    "nickname": "DeSo",
    "rewards": 0,
    "balance": bal,
    "account_number": "1234567891012136"
    }
    # Create a customer
    response = requests.post(
	   url,
	   data=json.dumps(payload),
	   headers={'content-type':'application/json'},
        )
    data1 = response.json();
    return data1;

customerId = "58282f94360f81f10454bd2a"
Bal = int(input());
aNum = "58283089360f81f10454bd2f";
textParameter = 1000;
list = [50, 400, 1200];

for i in range(0,3):
    amount = list[i];
    Bal = withdraw(Bal, amount);
	if(amount > textParameter):
		

cData = creAccount(customerId, Bal);
fBal = cData['objectCreated']['balance'];
print(fBal);
