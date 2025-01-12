import requests
import os
import json
env_var=os.environ
CHAT_ID = env_var['I']
TOKEN = env_var['T']
def get():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    a= r.json()
    return a




def get_id():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    a= r.json()
    return a['result'][-1]['message']['message_id']







def get_updates():

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    a= r.json()
    return a['result'][-1]['message']['text']







def send_message(text, chat_id):
    while True:
       url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
       params = {
        'chat_id': chat_id, 
        'text': text,
        'parse_mode': 'MarkdownV2'
        }
       r=requests.get(url,params=params)
       a=r.json()
       return a
matn=get_updates()
TEXT=f"||{matn}||"









def send_photo(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    photo_url = 'https://cataas.com/cat'
    response = requests.post(url, data={'chat_id': chat_id, 'photo': photo_url})
    return response.json()


def send_contact(CHAT_ID):
    url = f'https://api.telegram.org/bot{TOKEN}/sendContact'
    params = {
        'chat_id': CHAT_ID,
        'phone_number': +998991928213,  
        'first_name': 'Otabek'  
    }
    response=requests.post(url,data=params)
    return response.json()




def send_location(CHAT_ID):
    url = f'https://api.telegram.org/bot{TOKEN}/sendLocation'
    
 
    params = {
        'chat_id': CHAT_ID,
        'latitude': 41.2995,  
        'longitude': 69.2401  
    }
    
 
    response = requests.post(url, data=params)
    
    return response.json()


def send_dice(CHAT_ID):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDice'
    params = {
        'chat_id': CHAT_ID
    }
    
    response = requests.post(url, params=params)
    return response.json()



def send_audio(CHAT_ID):
    url=f'https://api.telegram.org/bot{TOKEN}/sendAudio'
    a='https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
    params= {
        'chat_id':CHAT_ID,
        'audio':a
    }
    response=requests.post(url,data=params)
    return response.json()




def send_venue(CHAT_ID):
    url=f'https://api.telegram.org/bot{TOKEN}/sendVenue'
    params={
        'chat_id': CHAT_ID,
        'latitude': 41.2995,
        'longitude':69.2401,
        'title':'SAMARKAND',
        'address':'UZBKISTAN'


    }
    response = requests.post(url, data=params)
    return response.json()








send_message(TEXT, CHAT_ID)
print(send_photo(CHAT_ID))

print(send_contact(CHAT_ID))
print(send_location(CHAT_ID))
print(send_dice(CHAT_ID))
print(send_audio(CHAT_ID))
print(send_venue(CHAT_ID))