import requests
import time
import uuid


def get_token(token):
    url = "https://token2go.p.rapidapi.com/api/v1/token/{}".format(token)

    querystring = {"t":"link"}

    headers = {
        "X-RapidAPI-Key": "74d87d1e7bmsh5d9ed7462b9236cp13302cjsn99cdf2426744",
        "X-RapidAPI-Host": "token2go.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.json())

def get_iss(iss):
    url = "https://token2go.p.rapidapi.com/api/v1/token/{}".format(iss)

    querystring = {"t":"iss"}

    headers = {
        "X-RapidAPI-Key": "74d87d1e7bmsh5d9ed7462b9236cp13302cjsn99cdf2426744",
        "X-RapidAPI-Host": "token2go.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

def create_token():
    url = "https://token2go.p.rapidapi.com/api/v1/token"
    ti = time.time()

    payload = {
	"rid": str(uuid.uuid4())[0:5],
	"url": "http://myurl.tld/subfolder/",
	"exp": 5,
	"iss": "MySystemIdentifier"
    }
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "74d87d1e7bmsh5d9ed7462b9236cp13302cjsn99cdf2426744",
	"X-RapidAPI-Host": "token2go.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    tf = time.time()
    delta = tf-ti
    print(" ### CREATE: {}".format(str(delta)))
    return response.json()

def delete_token(link):
    url = "https://token2go.p.rapidapi.com/api/v1/token/{}".format(link)
    headers = {
        "X-RapidAPI-Key": "74d87d1e7bmsh5d9ed7462b9236cp13302cjsn99cdf2426744",
        "X-RapidAPI-Host": "token2go.p.rapidapi.com"
    }
    response = requests.request("DELETE", url, headers=headers)
    record = response.json()
    print("## DELETED: {}".format(record.get('link')))
    return record



def remove_bulk_iss(iss='MySystemIdentifier'):
        
    record=get_iss(iss)
    items = record.get('items')
    total = record.get('total')

    for item in items:
        link = item.get('link')
        delete_token(link)


def create_token_bulk(nb):
    ti = int(time.time())
    for i in range(nb):
        token=create_token()
        print(token.get('link'))
    tf = int(time.time())
    delta = tf-ti
    print(str(delta))


#create_token_bulk(200)

#remove_bulk_iss()