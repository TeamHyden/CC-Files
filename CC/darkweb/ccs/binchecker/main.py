import requests
import json
import os
from colorama import Fore

def step2(bin):   
        api_key = 'a3eb03197f38fbed025a8c195d48c891b7d2a5fc'
    
        url =  f"https://api.bintable.com/v1/{bin}?api_key={api_key}"
        response = requests.get(url)
        print(response.status_code)
        try:
            print(response.text) 
            print(bin)
            response_json = response.json()
            if((response_json["message"]=="SUCCESS")) and (response_json["data"]["bank"]["name"] != ""):
                
                    print("\n______________________________________________________________________________________________________________\n")
                    print("Message : {}\n".format(response_json["message"]))
                    print(f"\nBIN NUMBER: {bin}\n")
                    print("Card type: {} {}\n".format(response_json["data"]["card"]["scheme"], response_json["data"]["card"]["type"]))
                    print("Country : {}\n".format(response_json["data"]["country"]["name"]))
                    print("Currency_code: {}\n".format(response_json["data"]["country"]["currency_code"]))
                    print("Bank:\n")
                    print("    Name: {}\n".format(response_json["data"]["bank"]["name"]))
                    print("    Website: {}\n".format(response_json["data"]["bank"]["website"]))
                    print("    Phone: {}\n".format(response_json["data"]["bank"]["phone"]))
                    print("\n______________________________________________________________________________________________________________\n")
            else:
                print(Fore.RED+" NOT VALID BIN!!!"+Fore.RESET)       
                pass
        except Exception as e:
            print(e)
            pass

bin = input('ENTER YOUR BIN: ')
step2(bin)