import requests
from api import LocketAPI
from auth import Auth
import json

print("Login")
email = input("Email: ")
password = input("Password: ")

auth = Auth(email, password) 
token = auth.get_token()

api = LocketAPI(token)

# account_info = api.GetAccountInfo()
# print(json.dumps(account_info, indent=4))  
# moment = api.getLastMoment()
# print(json.dumps(moment, indent=2))
response = api.updateGoldBadge()
print(response)