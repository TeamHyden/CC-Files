import requests


ss= requests.Session()

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Content-Length": "6251",
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

data = 'billing_first_name=%40zr4r_&billing_email=kjdkakjkd%40hotmial.com&order_comments=https%3A%2F%2Fwww.instagram.com%2Fp%2F&additional_comms=&sc_comments=followers%3Aundefined&wc_order_attribution_type=typein&wc_order_attribution_url=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_session_entry=https%3A%2F%2Ffollovery.com%2Fcheckout%2F%23&wc_order_attribution_session_start_time=2024-09-26+08%3A13%3A39&wc_order_attribution_session_pages=2&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+6.0%3B+Nexus+5+Build%2FMRA58N)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F129.0.0.0+Mobile+Safari%2F537.36&cf-turnstile-response=0._3vPPI2rMUuyFiugI3Nht-ul3vOxHNDTUv6lZrVqRLSQMFG9-ru68p4YgfqvINT7Splk8cXwm-gW_VQ_J8jO2UOXHZTGCS6XSQguL8mYmSjroCf1UUCeh7gSsdnN77saxsPyJNxCch3RlZyqfyGlJ0znBym6YqsQoqsY-lVT8j-ib7joFKJz1mspApoEiDxFjoSUw1v8Ebv41KTpno_MqaAjSBOVhoRuMxNSF_aXn_ak7oLXazsDIzPW27sJe34--xwtjzy6V1vxkb4fmnQKaFbqFpyOoQQyi_COAv-cevPNQAEteuz7SOCeF-abJ0aqvXjmxR5xvH6aErZBn1HsBL__QK7oirYaPWLx558dPd0-zW9OINsJYhkF767DBAbp8hQAIZoTFZ2LH32sxQ4zxacBq61JUdUlzO6XTNva6x3sUc7g6gj_T7aiNw5lLWGnRhfXuTJk8WpIUXWM8jFaWvaDQBMt9ES2tUh2t4uHmJj7J2ni6xb2-u9NFXop_3h-Qt9vvYBZ7zsDSYXDeAvBR6uCLFps8LFDgalY1CZckvnrTkefLnv6v_bPGEqAjyUle-23KPsbc9DEhpWPxDybXsinQxoG9LadycRVxyVdCS3_1Uzx3FhqOzlF25jf_q2ipKB0vYgL9UcEN8_UPKKG13iNN6rKY71yd6yOchp3f5TCe372OVc0qse40RVPG0IU-_gPO3_dSTilyGA6XSfOL09BPWtY9Cgpr0pWoIfCtFzauV29RJI5Hw1_U5kLbSAfXn90P5tOjCDqxtVPZqxXrhafFcbm7GmFISq-TmL2GuJlwStQuNKYeOoAuc05QUq6zWGF3y2UIVvr5WXkwLMYqg.7BUv7cTf0X4rxT4BB2Lifg.74706b6ca4edbb3429c06e948632f885c98f07944a6341c66718e93e60ccb940&coupon_code=&payment_method=stripe&woocommerce-process-checkout-nonce=1db97b8faa&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&stripe_source=src_1Q3Dv0FFQtUFwFVVx65MoDsm'

res = requests.post('https://r.stripe.com/b',data=data,headers=headers)


print(res.text)