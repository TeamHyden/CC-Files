import requests

session = requests.Session()

#hcaptcha_token = "P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoialpGL3pRRHN3UnR6U0dYajlKTFhrTDNBdXpjZi90MGJNYWpDbFhHNDlubFRTZEVWSFd5SEFxQWdzbjF6TXhrWFVyVjRIWkExTVh4V01iTVRVZ2ZYUU83a3lSa0tuVlp6MzlKVzdEU2s1dU4xeC9qZldRTkx4c01wRzZFc0svTGZyQVhiN3lkNXl1RTRsRnAxak5YZVFKQUhQL2h2K3JQVWs5Z2trOGo5VFl6UFU5ZjYvZllmbXJORCtZdEp3Y2pSRzVXbEdNKy9IMEQrVFFvTVFGWHFiY0pJUlhxWGh4RlFOR1NGNDZqSjNoMzJteVdBR1dMQUExRlVPNzMrc0lTc0JFSDBYcVl4SHBUWXNHOTliUFJJK1pKbnhpRlBEREtlZGp2YkE4MjdpellPUEtTTDU1T2YvZ1NHcmsrendjci9KM1c4SU9yOGE1YUZBb0UwSU9nM1pzZThTRXVNMmF6ZnFDUTdtTzM3ZlVPMS8zclhtR1ZxKzNMWUFMTFZtOVZnN2x2TzVqRkZNRHhhSStYd1BScVZWMG5uVjFKNTU3WS9YUThqRDBNNVE3Yy83dVpma0R3RkVONXZraU1QZzdGK2R6TXRnTTBmSCtzR2VrMnpUS1pSWHN2TWhVbGhLQ0J1b0RqMWNhWjRQOWluZzBFMENtWkpuaSsxVWZJMXNmdXRQMUdnam5odzFnaVd5Nzl5NkFIMC9rb2I0VUhvcFJzL09NZ1p3VEVmSjB0M3lka2p1bStvbElwY21vNEJDaFR6R0E4emVxSXlRbldjb012dzBDTXJRNitTTDlvMXJQZXdtaXVCS2VBTG1KNXBhaVVBM21uUFZzNDZpbXhoeDZTY0c5SDJIMC9QTjVOS2VHQ1djK0RsMDdyQkZpYTUyL1dROEJHUS82cjJmaXdjcVNhVE9mejJtcEluNEhaeGMreFZJMUdZY3dBZlRnaGI0NGhnWkg0bVpBekxKTktHK2lqSnQxWk9PQ3FWeXBBNWlyUlZzejAzdHViNWtqMldmSjlmN2xBWG1TRmlmYVZtVGk5SThZR1dsckdYV2hCekE5MlBudW5nQWNienlXWmwxMG91am82ZU53VUlUUnFLcUhEZzV1MFBPV01qRkEzU2czQkhuNkFxWEFJRzE4M1llb24rR2tLQkV0SHVxRVV6ZGRRZDBBUTlGRkMrQjkyMEFncmZ6L201ZmpvblpJczd6cU9lV3BXVEFrajdqSU82bmJoK09VUUxTK2ZieGNXbE9yOWx5SWg4M29xTklCamxCZXBBYjRadDBWeHJ3QlZsOWl0dnhWa2owQy9ReTNTQlhiNjdzeFhqSUhCNk9LVTFBMm1Tdll0NDREdG1SSzlCMG1MSi83N3BlVTB2cXluenFZbU8wTU82ZStwcWxmVFlMczVNeld5b0llWlNUc1g3VEpndVpsWVhpamgwdTBlOUZHVittSDJzUjVYdWFaTU9USmNHUjRwVXRVNm5CYUJtU01wbEhaS216RjRyalQ0SU5ZUmlkUTZKN2dHU2xybzNZR1ZhM3R0NXo0OFNCRFgvb0lZOXdSZit0NHFZSnM5T1Z5aUNBVlV3VThkWURaeTJwTWo4OG1RZGFBWGtvbHk1ZjdkeEk1ZWw1TFJRK1Bwby82V0I0Y0lWVzk2Yjd2QWFZSUVVVkxZTy96QnE4YlBueWZORU5XYnFNSUNPaTZVNEQwUC9VRDM4N1pPaHcwcS82RE5rMHZNL2lDdlk4YTZQLzJUVFl1ZUIvOUwwdllPOXFVZGRoajY4cnV0dWQ2S2xoaHorYmoxQU1YYTdKNUwrYlc0RDVLdjdYeHRZMk9CemZIWGN3LzJVZXpsK3d3WGxaV0szcHg5STR0Z3lpSTlGUmltODRyQk5aUm5uZWhyVVdzNWNzMEorTWw2dFhWajZhcnNpdmVhRE5MN3p0M1lveDNzZi9iRjVmdTBWcFpxUEkvM01GSlFoZjRpSE5zZ3MrQUxxWk9EZTYwL0o3RDhJOVVsVmNybllUMjdGQXU0dVdlQTUvOW5QdnFNY1RDZEhMVklmTWEzNGRaM1A4RFEvbVR1WXB1NmpDSlBxNFZocG4rYzVlZU5FMWVwVStTc3dJUHY0YWNWRUpQVTA0K0F6UlAwc2hsdFM1RWJKMmg3SW1yejFoV1cxdjk5TFpxSFRRZEVrTFRaNlI2M1RlWDE2NlVNNVE4dTVZZk52RTZ6T3lSSUt2Q1I2bHk4WXVnTmNiSXl3NkRjTzlwZzVYZkhYajNZcmR1SUdIc2pCdVVXRFlZU3Y5UnE3cmZXRnhlN0VBVnhmS2VPOVRjdWcyVEI0ZlpEbnNMaFc4Nk5TdjlWQ0lDRUFyRDlWeVMvSjdhT0s3c2tTTUhwUFRSb3pwdmFSa25LK21nMGRybnRFeDN6ci9OenhTNGJBcTNVT2ZGa2FSa2gvVmhJcmJxcmJYczl4ZGMzNFFkK0xDQUY4aDNMdVJFOXl2OE5uUHhHSEtnRW5sT3ltcTM5b0VBODNlWGpUVFlxVVNURHNLQ3RDREI4aUp4UHBlUWllRmRuU0xhaGpjajdETGltS1VhbGZlRVM4bTY2RnZrS3pETU53VWxvM1cyTjJRUlNMSU81NHNvTGhnWUJIT3Bzd0RMZEtqNUZseGl6bHBoRXRMYTRDU2NVTGtrYW12QUI4VGVqUm9PL1dqckl6eVY1bmg5Q0oxM3YySldEdXJJU29FWVladEJUc3RzRmgzRmhWNXp5bkRUNURpTW5TejZmbHRRM3I3R1JvM0NEc24vNVFDdUN0SU9hQ2NtbmhVVTV2QjA4U21KVE5HY2JvY2Yvd3dHMjFIcXpyR01DQ2xpbEpqdDVRL3UrWXU1dU5EeCtnRFFmQzJqRzl3QT09IiwiZXhwIjoxNzI3MzQwMzUxLCJzaGFyZF9pZCI6MjU5MTg5MzU5LCJrciI6ImI0ZDUzZjIiLCJwZCI6MCwiY2RhdGEiOiIrQzRMdm1zKzUyZU5UQUFJejB3SmhpQWNNdm5qa2pZNVg4WHVaNEJCTHVsU05nd1lBU0ozNktlVnV5c0NoUC9Od2F6aENOTVNWWjE1MGFXS2ZsQWtYcy9sV0s3b2ZJYlRUZThSeGxnZjQrcVBFU2ltUGlENHg4S3JHOXJhOVlUYTJSZEtWV3FCaDBxcFdvU3ZPYmhObUpWWlBDN1RIR1NiQWhCVE8yMnRUandZUm0zbnA1U1EvUUdHbzZoVEk1OTlJL1FNM25UTUNzeElYczFnIn0.Rma2sPSkdEW9AVlTblPnvtSRFZTYA_3LLSY7Ih5271E"
#    "radar_options[hcaptcha_token]": hcaptcha_token
pk ='pk_live_xHPYiDPVVFb6I9qV8dUyxUvZ00WAfN6fFs'
data = {
    "type": "card",
    "card[number]": "53635000072203",
    "card[cvc]": "119",
    "card[exp_month]": "05",
    "card[exp_year]": "27",
    "owner[name]": " ",  # Add your name
    "owner[email]": "akjdfljajld@yahoo.com",  # Add your email
}

headers = {

    "Authorization": f"Bearer {pk}",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://js.stripe.com",
    "pragma": "no-cache",
    "referer": "https://js.stripe.com/",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "User-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}

# Send the POST request to the Stripe API
res = session.post('https://api.stripe.com/v1/sources', data=data, headers=headers)
print(res.text)


print("STEP 2 \n\n")

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Content-Length": "2011",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://follovery.com",
    "Pragma": "no-cache",
    "Priority": "u=1, i",
    "Referer": "https://follovery.com/checkout/",
    "Sec-CH-UA": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "Sec-CH-UA-Mobile": "?1",
    "Sec-CH-UA-Platform": "Android",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

data= 'billing_first_name=%40zr4r_&billing_email=kjdkakjkd%40hotmial.com&order_comments=https%3A%2F%2Fwww.instagram.com%2Fp%2F&additional_comms=&sc_comments=followers%3Aundefined&wc_order_attribution_type=typein&wc_order_attribution_url=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_session_entry=https%3A%2F%2Ffollovery.com%2Fcheckout%2F%23&wc_order_attribution_session_start_time=2024-09-26+08%3A13%3A39&wc_order_attribution_session_pages=2&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+6.0%3B+Nexus+5+Build%2FMRA58N)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F129.0.0.0+Mobile+Safari%2F537.36&cf-turnstile-response=0.xq0vplskdKWCqHesVHYFhPfsG37n7uZTio59vLjdbnjGk3k7oyMWgKp9WC5InPdzDW1-25D38UYknxRry54OXVW5hfaMyOo0qJe2AJI86RvgW2Ssoykaod-xgoBThg0fxCaCfI8eWgx7XazefxyHf0Ng8EgQWasRmNt4YhutJQoFegSeUzmVrHpXcv-c4NNgEJaXood2Y4zVVFrdly6b7pyGmnt9cnBsRPcJl48pYlWrLH6nWZ58lij9DyR5bu0UpNKncGN1SKn3KC0WZklrVFvEQfdGrP349ghCFrDQemEjg1QcY-gCVEl2I9zMpN2MjNU5HajmQjozFiFm_jQQ1rjZpKvLIv2Vx4uLxr_aJn9ahgg3icbs9w7MNMklxEqzXe9HyvMcQjRZB2sDgC43pqNDOzELtns_pBZjXj7PDQVtFkdOqT7Qi1MBENIZ2-UvPFGsC2om2BZGcgvIzMnze4rd_PLlqbW53FPGCreyXCR4lZioi0ANs1AHx6GUSK838x5oKAwYDzJBFyeq25XTatF0XBppnBVWPr_tugesAm25PgTgDKxTSoG4khZtzPp0xQDULS-K18EnBGPmyhb8qPVd1NVFxhPsEMRp5ioI1_IPWjyMBf1Nt7_9crJHzAL89J7bCc2pj0ER4TEyjsIeonteFr7VAbNW-rlyOBBsPm_dnPwBTTDhOVlbrd4x4jtSOI_lh1jF3X-cStlM9sLn36RQGhQ2nuFZa57Ux4SoIgWHcuZDfdWIL63npDdZsoyMCaUGfUNmgmRjuWxvPc8ASEK2QOFUF69w0XfOUDxYxqlHS7_zmoawYRSbCZ-H0_d8Y0rvzlqzfzpWsaCJ98XfCw.Ull7y5pTPQzfeE8vtZhBgQ.6d7b4939676d01388fbcf9e9d9cb21a34d7b3146fccc426c981d47da887f2661&coupon_code=&payment_method=stripe&woocommerce-process-checkout-nonce=1db97b8faa&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&stripe_source=src_1Q3DRtFFQtUFwFVVSPwSdOlX'

res = session.post('https://follovery.com/?wc-ajax=checkout',data=data,headers=headers)

print(res.text)


print("step 3\n\n")

data ={
'is_stripe_sdk': 'false',
'client_secret': 'pi_3Q39mRFFQtUFwFVV0CeA61Me_secret_jz9gXcokvEn8JTBbAx2EN1rgi',
'key': f'{pk}',
}


headers = {

    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://js.stripe.com",
    "Pragma": "no-cache",
    "Priority": "u=1, i",
    "Referer": "https://js.stripe.com/",
    "Sec-CH-UA": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "Sec-CH-UA-Mobile": "?1",
    "Sec-CH-UA-Platform": "Android",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}
res =session.get(f'https://api.stripe.com/v1/payment_intents/pi_3Q39mRFFQtUFwFVV0CeA61Me?is_stripe_sdk=false&client_secret=pi_3Q39mRFFQtUFwFVV0CeA61Me_secret_LHhcIbn56wyOKV2L1WMWiJNC&key={pk}',data=data,headers=headers)


print(res.text)