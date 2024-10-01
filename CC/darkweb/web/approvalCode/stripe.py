import requests
import string
import json
import urllib.parse

session = requests.Session()




def keys():


    headers = {
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-US,en;q=0.9",
  "Authorization": "Bearer 198eJlUPOMQrPAzEQrcuUD5edZYqSpUIFdcu6svtfPCFanXyn4p",
  "Cache-Control": "no-cache",
  "Origin": "https://js.chargebee.com",
  "Pragma": "no-cache",
  "Priority": "u=1, i",
  "Referer": "https://js.chargebee.com/",
  "Sec-Ch-Ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  "Sec-Ch-Ua-Mobile": "?1",
  "Sec-Ch-Ua-Platform": '"Android"',
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-site",
  "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
    res= requests.get('https://tryhackme.chargebee.com/api/internal/payment_intents/fetch_gateway_public_credential?origin=https:%2F%2Ftryhackme.chargebee.com',headers=headers)
    json_data = res.json()
    pk = json_data['publishable_key']
    return pk
   
keys()