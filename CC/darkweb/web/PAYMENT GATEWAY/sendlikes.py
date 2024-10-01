import requests
import random


ss = requests.Session()
def generate_code():
    prefix = 48
    suffix = str(random.randint(100000, 999999))
    return str(prefix) + suffix



for i in range(0,20):
 uid = generate_code()
 headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Content-Length": "125",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-26%2004%3A06%3A24%7C%7C%7Cep%3Dhttps%3A%2F%2Ffollovery.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-26%2004%3A06%3A24%7C%7C%7Cep%3Dhttps%3A%2F%2Ffollovery.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; cookieyes-consent=consentid:a0luUlByM3NGTFp2dkMyQkJXdHoxdHFVeHI2TEM5Yms,consent:no,action:,necessary:yes,functional:yes,analytics:no,performance:no,advertisement:no; _ga=GA1.1.1301770897.1727325399; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ffollovery.com%2Ffree-checkout%2F; _ga_0JB1PNKTFG=GS1.1.1727325399.1.1.1727325728.0",
    "Origin": "https://follovery.com",
    "Pragma": "no-cache",
    "Priority": "u=1, i",
    "Referer": "https://follovery.com/free-checkout/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "Sec-CH-UA-Mobile": "?1",
    "Sec-CH-UA-Platform": "\"Android\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
 
 data = {
'profileId': uid,
'postUrl': 'https://www.instagram.com/p/DAXgbp3oH3j/',
'email': 'alexcost45a@dygovil.com',
'username': 'zr4r_'

}
 res =ss.post('https://follovery.com/custom/api/sendlikes.php',data=data,headers=headers)
 print(res.text)

