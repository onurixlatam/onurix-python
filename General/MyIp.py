import requests
headers ={
'Accept':'application/json'
}

r = requests.get('https://www.onurix.com/api/v1/my-ip', headers = headers)

print(r.json())
