import requests
import random
import json
import urllib3
from colorama import Fore
import requests
import requests
import re
import zstandard as zstd
import gzip
import zlib
from fake_useragent import UserAgent
import random
import json
import brotli

valid_bin = []

randomnumbers = [

319990,
337941,
377940,
377941,
377946,
377948,
400227,
400228,
400256,
400290,
401325,
401345,
402166,
402330,
402331,
402358,
402375,
402725,
402859,
403372,
403656,
403824,
403845,
404193,
404248,
404249,
404733,
404734,
404742,
404747,
404780,
404790,
404791,
404988,
405166,
405167,
405621,
405670,
405671,
405672,
405782,
405783,
406307,
406322,
406323,
406325,
406326,
406328,
406329,
406330,



]

def step2(bin):   
             
        api_key = '5db83c0f47ee000942567f087e933955086f19b1'

        url =  f"https://api.bintable.com/v1/{bin}?api_key={api_key}"

        response = requests.get(url)
        print(response.status_code)
        try:
         print(response.text) 
         response_json = response.json()
         if(response_json["message"]=="SUCCESS"):
            with open('PolandBINS.txt','a') as f:
                f.write("\n______________________________________________________________________________________________________________\n")
                f.write("Message : {}\n".format(response_json["message"]))
                f.write(f"\nBIN NUMBER: {bin}\n")
    
                f.write("Card type: {} {}\n".format(response_json["data"]["card"]["scheme"], response_json["data"]["card"]["type"]))
                f.write("Country : {}\n".format(response_json["data"]["country"]["name"]))
                f.write("Currency_code: {}\n".format(response_json["data"]["country"]["currency_code"]))
                f.write("Bank:\n")
                f.write("    Name: {}\n".format(response_json["data"]["bank"]["name"]))
                f.write("    Website: {}\n".format(response_json["data"]["bank"]["website"]))
                f.write("    Phone: {}\n".format(response_json["data"]["bank"]["phone"]))
                f.write("\n______________________________________________________________________________________________________________\n")
            valid_bin.append(bin)
         else:
             print(Fore.RED+" NOT VALID BIN!!!"+Fore.RESET)       
             pass

        except Exception as e:
            print(e)
            pass


for i in range(0,len(randomnumbers)):
    step2(randomnumbers[i])
