
import requests
import string
import json
from fake_useragent import UserAgent
from colorama import Fore

ccn= '4430400048039923'
cvv='179'
exp_month='07'
exp_year='2026'
session = requests.Session()
def phrase1():
    def braintree():
        data = {
    "clientSdkMetadata": {
        "source": "client",
        "integration": "custom",
        "sessionId": "21c2327f-9577-44e6-bdea-c34f88450983"
    },
    "query": """
        mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {
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
        }
    """,
    "variables": {
        "input": {
            "creditCard": {
                "number": ccn,
                "expirationMonth": exp_month,
                "expirationYear": exp_year,
                "cvv": cvv,
                "billingAddress": {
                    "postalCode": "90310",
                    "countryCodeAlpha2": "US"
                }
            },
            "options": {
                "validate": False
            }
        }
    },
    "operationName": "TokenizeCreditCard"
}

        headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjczMjkyMDIsImp0aSI6IjNhNjhiZTdjLTc1ZmUtNGJiMy05YzhiLWE3OTA1YzIwNDlhYiIsInN1YiI6InN4ODk1c3ZuOWI5Y2hodjUiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InN4ODk1c3ZuOWI5Y2hodjUiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.J18d4HfmiZj3H7l7lR6c0x34DiM7Mn4vzcLs6A53eQIiEkzekYnixE86ONVVUoZiMFaNY_DNu-0FdPU33j3w0Q',
    'Braintree-Version': '2018-05-10',
    'Cache-Control': 'no-cache',
    'Content-Length': '820',
    'Content-Type': 'application/json',
    'Origin': 'https://study.com',
    'Pragma': 'no-cache',
    'Priority': 'u=1, i',
    'Referer': 'https://study.com/',
    'Sec-Ch-Ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'Sec-Ch-Ua-Mobile': '?1',
    'Sec-Ch-Ua-Platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'
}
        response = session.post('https://payments.braintree-api.com/graphql',headers=headers,json=data)

        response_json = response.json()
        print(response_json)

        if response_json["data"]["tokenizeCreditCard"]["creditCard"]["binData"]["productId"]:
            print("We found it!")
            token = response_json["data"]["tokenizeCreditCard"]["token"]
            headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Content-Length": "532",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://study.com",
    "Pragma": "no-cache",
    "Priority": "u=1, i",
    "Referer": "https://study.com/academy/get-started.html?product=CEN",
    "Sec-CH-UA": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "Sec-CH-UA-Mobile": "?1",
    "Sec-CH-UA-Platform": "Android",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
    "X-CSRF-Token": "41d08247-763a-43a4-a908-c26646bf71e9",
    "X-RequestGuid": "bccc95b24c616e7827eab6f0d1d2617c",
    'Cookie':'hasSeen=true; JSESSIONID=0A1C59CF5B94AC085BA91DC40497FF6D; ariel=1e75f2befd2cf396be35f0f6e55f55fa; aens=enp; _sv=D; _idsv=D; cocoon=""; NODEID=8653ef2b; _gcl_au=1.1.556018930.1727242245; sa-user-id=s%253A0-b6751bc9-bbc5-4b32-6ddc-403b4b70318b.WnkJM71LwdOBdSTUSQ094HmMF5WZy%252BaBerZSCi5a4Kk; sa-user-id-v2=s%253AtnUbybvFSzJt3EA7S3Axiw.j%252FNx8q1GNdOZ1c0jKadopzcAuHf0hrtAwrMTLCJJ4N4; sa-user-id-v3=s%253AAQAKIJjgYkpJ3HruqyiMWxTvP8RH78GTNZszsAJmv3dJXbogEOQBGAIg7vzKtgY6BNu6vxlCBFjwk2U.csT8yASxjmuDH%252FHF4MNbnuA290nXOQH%252FdyAG7XIwozQ; _fbp=fb.1.1727242262370.94575844149854278; hasSeen=true; __stripe_sid=feb42839-44cd-47aa-a0f1-6ccafa75a110fd4e6b; __stripe_mid=94aeb1f1-2fa9-4cb6-a564-1106b0ca3ee9fb66c4; ssoe_debug=alwaysOnCtaLanguage-signUpNow.braintree-V3.breakthroughLogo-v2.cxSocialProof-control.dummy20240529-test.eagerlyRenderPartialRegModal-x.emphasizeCoupon-x.globalCssDefer-v1.nitpuxAIAssistant-x.printQuizReactPage-v1.reactSchoolCredit-x.renameCX-saver.smsAcquisitionV3-control.testPrepAiAssistantBeta-x.testPrepIntegratedUx-v4.testPrepYoutubeVideoSection-x.updateCxRegFlow-x.userTypeGoalSidebar24Q3-x; surveyCriteriaUrlPatterns=INVALID_INELIGIBLE; requestGuid=bccc95b24c616e7827eab6f0d1d2617c; _rdt_uuid=1727242250348.d7d92434-6a1b-4a42-b9ef-0e8246f4dbc0; _uetsid=52fa6c407aff11efb8f6cd86507bdd09; _uetvid=52fbe9107aff11efb8487ff88e8f09c2; datadome=rpaQJGHSN~aCH~23CNHoRBQ6fP6~k4yIOE8Jm5DKfvpSVV5zJhMJt0GbclPP4iOpEa~ONd~34cUEd7S7ZLfK2t3_xakGoDoIn5DB1nq5AJhwgxB7Gyrkg4pN8zpkNl5_'
}
            data = {
    "isSpecificTestPrep": True,
    "product": "CEN",
    "currentProductBillingTerm": "MONTHLY",
    "paymentMethod": "BRAINTREE",
    "userType": "INSTRUCTOR",
    "goals": "TEACHER_CERTIFICATION",
    "examName": "CEN",
    "email": "alexcosta@dygovil.com",
    "password": "alexcosta@dygovil.com",
    "passwordConfirm": "alexcosta@dygovil.com",
    "billingAddressCountry": "US",
    "billingFirstName": "ALEX",
    "billingLastName": "COTA",
    "billingAddressZipCode": "93506",
    "phoneNumber": "+12085689244",
    "verificationToken": token,
    "token":token,
    "paymentGateway": "BRAINTREE",
    "paymentType": "CARD"
}
            response =session.post('https://study.com/academy/register/subscriber/submit-subscriber.ajax',data=data,headers=headers)
            print(response.text)
        else:
            print(Fore.RED+"CARD NOT VALID"+Fore.RESET)    
    
    braintree()

phrase1()