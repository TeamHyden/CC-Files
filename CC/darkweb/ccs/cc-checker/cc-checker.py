import requests
import string
import string
import json
from colorama import Fore
import random

session  = requests.Session()
def step4(usercard):


    # Inner function to validate a credit card
    def cc_validity(cc_usr, full_cc):
        try:
            # Get CSRF token
            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
            }
            random_number = "95" + str(random.randint(10**10, 10**11 - 1)).zfill(11)

            # Request to get CSRF token
            response = requests.get(f'https://dnschecker.org/ajax_files/gen_csrf.php?upd=1010.4088647253607', headers=headers)
            json_data = response.json()
            csrf_value = json_data['csrf']

            # Validate credit card number
            url = f'https://dnschecker.org/ajax_files/credit_card_validator.php?ccn={cc_usr}'
            headers.update({
                "Csrftoken": csrf_value,
                "Referer": f"https://dnschecker.org/credit-card-validator.php?ccn={cc_usr}"
            })

            response = requests.get(url, headers=headers)
            result = response.json()

            # Check validity of the credit card
            if result["results"]["luhn"] == 0:
                print(Fore.RED + "Invalid number" + Fore.RESET)
            else:
                print(Fore.GREEN + f"Valid number {usercard}" + Fore.RESET)
                
               
        except requests.exceptions.RequestException as e:
            print('Error making request:', e)

    value = usercard.strip().split("|")[0]  # Extract the credit card number
    cc_validity(value, usercard)  # Call the inner function to validate


usercard = input("Enter Your Card: ")
step4(usercard)