# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

#POST https://api.twilio.com/2010-04-01/Accounts/AC123456abc/Messages
# Find these values at https://twilio.com/user/account

account_sid = "ACf5a26da9bb7bb91160601fc32921b0d7"
auth_token = "2899c0df8f7c7864083cfd74320b0bdc"

account_sid1 = "AC71921bf4ee31c65e6f0c3404fc09c1c0"
auth_token1 = "f5e90af15a8e6001f821cee512ae1749"

client1 = TwilioRestClient(account_sid1, auth_token1)
client = TwilioRestClient(account_sid, auth_token)


message = client.messages.create(to="+17204800272", from_="+17205731824",
                                     body="Hello there!",
                                    media_url = ['https://demo.twilio.com/owl.png', 'https://demo.twilio.com/logo.png'])

message1 = client.messages.create(to="+17202265792", from_="+17205731824",
                                     body="Hello there!",
                                     media_url = ['https://demo.twilio.com/owl.png', 'https://demo.twilio.com/logo.png'])
