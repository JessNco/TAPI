import requests
from requests.auth import HTTPBasicAuth
from datetime import date

basic = HTTPBasicAuth('rttapi_JessNco','ef910c941df65dcc97d7ffa0dee01eb6980dcba0')

def valid_request(x):  #checks for valid request (to do make a proper error)
    y = x.status_code
    if y == 200:
        return x
    else:
        return "Error"

def departures(x): #pulls departures from a station needs CRS or TIPLOC
    u = 'https://api.rtt.io/api/v1/json/search/' + x
    return valid_request(requests.get(u,auth=basic))

def depart_to(x,y): #pulls departures from a station to a specific destination needs CRS or TIPLOC
    u = 'https://api.rtt.io/api/v1/json/search/' + x + '/to/' + y
    return valid_request(requests.get(u,auth=basic))

def train_info(x): # pulls train info from service UID
    today = date.today()
    y= today.strftime('%Y/%m/%d')
    u= 'https://api.rtt.io/api/v1/json/service/'+x+'/'+y
    return valid_request(requests.get(u,auth=basic))

