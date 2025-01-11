import requests

TOKEN ='1602686596:AAHdqoVLsAlXlFYDlihaQy1x_Tmilg7fqiM'

URL = f"https://api.telegram.org/bot{TOKEN}"

# Get me
r = requests.get(URL + "/getMe")
print(r.json())