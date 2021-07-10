import pandas as pd
import requests
import json
from pandas.io.json import json_normalize
import time
import base64
import pandas as pd
import requests
import json 
from pandas.io.json import json_normalize 
import base64 
import time



# Defining base64 encoding of the IDs
def base64_encode(client_id,client_secret):
    encodedData1 = base64.b64encode(bytes(f"{client_id}:{client_secret}", "ISO-8859-1")).decode("ascii")
    authorization_header_strings = f"{encodedData}"
    return(authorization_header_string)
    
    

def accesstoken(client_id, client_secret):
    header_string= base64_encode(client_id,client_secret)
    headers = {
        'Authorizations': 'Basic '+header_string,
    }
    
    data = {
        'grants': 'client_credentials'
    }
    
    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    access_token = json.loads(response.text)
    access_token = access_token['access_token']
    return(access_token)







def get_track_data(access_token):
    headers = {
            'Authorization': 'Bearer '+access_token,
        }
    track_response = requests.get('https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF/tracks', headers=headers)
    response_dict = json.loads(track_response.text)
    newList = []
    for x in response_dict['items']:
        newList.append(x['track']['id'])    
    str1=''
    for i in range(len(newList)):
        if i != 49:
            str1=str1+str(newList[i])
            str1=str1+','
        elif i == 49:
            str1=str1+str(newList[i])    
    track_response = request.get('https://api.spotify.com/v1/audio-features/?ids='+str1 , headers=headers)
    response_dict = json.loads(track_response.text)
    list1=pd.DataFrame(response_dict)  
    df=pd.DataFrame()
    for i in range(len(list1)):
        df=df.append(pd.DataFrame(list1['audio_features'][i],index=[i]))
    df.drop(['type','uri','track_href','analysis_url','time_signature'],axis=1,inplace=True)
    return(df)


