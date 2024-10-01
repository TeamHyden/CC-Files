from flask import Flask, request, jsonify, render_template, send_file
import random
import requests
from colorama import Fore
from flask import Flask, request, jsonify, render_template, send_file, send_from_directory
import os
import random
import json
import urllib3
from colorama import Fore
import requests
import requests
import re
from flask import url_for
from flask import redirect
import zstandard as zstd
import gzip
import zlib
from fake_useragent import UserAgent
import random
import json
import brotli





app = Flask(__name__, static_folder='static', static_url_path='/static')

valid_bin = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_bin', methods=['POST'])
def generate_bin():
    file_path = os.path.join(os.path.dirname(__file__), 'Validbin.txt')
    selected_value = request.json['selectedValue']
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('')  # create an empty file
    # Call the step1 and step2 functions
    randomnumbers = []
    def step1():
        def generate_random_number():
            while True:
                num = random.randint(10000, 99999)
                if str(num)[0] not in ['0']:
                    return int(selected_value + str(num)) 
        for _ in range(20):
            randomnumbers.append(generate_random_number())

    def step2(bin):   
        api_key = 'd71376b0700c7f0d519357f6371b56eb680a4308'
        url =  f"https://api.bintable.com/v1/{bin}?api_key={api_key}"
        response = requests.get(url)
        print(response.status_code)
        try:
            print(response.text) 
            print(bin)
            response_json = response.json()
            if((response_json["message"]=="SUCCESS")) and (response_json["data"]["bank"]["name"] != ""):
                file_path = os.path.join(os.path.dirname(__file__), 'Validbin.txt')

                with open(file_path,'a') as f:
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

    step1()
    for bin in randomnumbers:
        step2(bin)

    # Return a success response
    return jsonify({'success': True})

@app.route('/download_page')
def download_page():
    return render_template('download_page.html')

@app.route('/download_validbin')
def download_validbin():
    file_path = os.path.join(os.path.dirname(__file__), 'Validbin.txt')
    return send_file(file_path, as_attachment=True, mimetype='text/plain')

@app.route('/ccgen')
def ccgen():
    return render_template('ccgen.html')





@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

from flask import Flask, request, jsonify, render_template
import requests
import random


def step3(bin):
    # Generate a random year
    random_year = random.randint(2024, 2033)
    data = {
        'type': 3,
        'bin': bin,
        'date': 'on',
        's_date': '',
        'year': random_year,
        'csv': 'on',
        's_csv': '',
        'number': 1,
        'format': 'pipe',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Length': '85',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_ga=GA1.1.1545944997.1726592715; __gads=ID=cad82750607ea73d:T=1726592715:RT=1726596120:S=ALNI_MZc7xnYYOukeIXOm-fsYFqiXtyVhg; __gpi=UID=00000f0ed1e914ef:T=1726592715:RT=1726596120:S=ALNI_MauTTShSEUwHkOogX4GiZyy1KfSZQ; __eoi=ID=33ca3de5ae284dad:T=1726592715:RT=1726596120:S=AA-AfjYU9k8vT2qeGGm1PB0Y8TmS; _ga_SFSXHF70Y1=GS1.1.1726594833.2.1.1726596123.0.0.0; FCNEC=%5B%5B%22AKsRol_lJbbVY0rb0QNJFq4UNVpCuwSjNlONLBLi0CdGjZFAwgXnHdlEjPcKxPKExYHmQoXjtCy4kVuKw1qJRfXbmBR6fkOCEFvqiCdw-msOzIKw-6i0x3FeVoC3DQgZRXlRUfQ1N4a_0WPKzLeDFbGCNR0jnKwc0w%3D%3D%22%5D%5D',
        'Origin': 'https://namsogen.org',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://namsogen.org/',
        'Sec-Ch-Ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': 'Android',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post('https://namsogen.org/ajax.php', headers=headers, data=data)
    result = decoder(response)
    return result

def step4(user_input_cc):
    def cc_validity(cc_usr,full_cc):
     try:
        # Get CSRF token
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Priority": "u=1, i",
            "Referer": "https://dnschecker.org/credit-card-validator.php",
            "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": "Android",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36",
            "Cookie": "_lc2_fpi=00849f875789--01j8a35hpsh2r8414sxt09fezj; ... (rest of the cookie values)"
        }
        random_number = "95" + str(random.randint(10**10, 10**11 - 1)).zfill(11)

        response = requests.get(f'https://dnschecker.org/ajax_files/gen_csrf.php?upd=239.{random_number}', headers=headers)
        json_data = response.json()
        csrf_value = json_data['csrf']

        # Validate credit card number
        url = f'https://dnschecker.org/ajax_files/credit_card_validator.php?ccn={cc_usr}'
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Content-Type": "application/x-www-form-urlencoded",
            "Pragma": "no-cache",
            "Priority": "u=1, i",
            "Csrftoken": csrf_value,
            "Cookie": "_lc2_fpi=00849f875789--01j8a35hpsh2r8414sxt09fezj; ... (rest of the cookie values)",
            "Referer": f"https://dnschecker.org/credit-card-validator.php?ccn={cc_usr}",
            "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": "Android",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        print(response.text)
        result = response.json()

        if result["results"]["luhn"] == 0:
            print(Fore.RED + "Invalid number" + Fore.RESET)
        else:
            print(Fore.GREEN + "Valid number" + Fore.RESET)
            with open('LiveCC.txt', 'a') as f:
                f.write(f'{full_cc} \n')
     except requests.exceptions.RequestException as e:
        print('Error making request:', e)





    results = []
    for i in range(0, len(valid_bin)):
       result = step3(valid_bin[i])
       results.append(result)


    for result in results:
           value = result.strip().split("|")[0]  # extract the credit card number
           cc_validity(int(value), result)


def decoder(response):
    content_encoding = response.headers.get('Content-Encoding')
    try:
        if content_encoding == 'br':
            return brotli.decompress(response.content).decode('utf-8')
        elif content_encoding == 'gzip':
            return gzip.decompress(response.content).decode('utf-8')
        elif content_encoding == 'deflate':
            return zlib.decompress(response.content, -zlib.MAX_WBITS).decode('utf-8')
        elif content_encoding == 'zstd':
            dctx = zstd.ZstdDecompressor()
            return dctx.decompress(response.content).decode('utf-8')
        else:
            return response.text
    except zstd.ZstdError as e:
        print(f"ZstdError: {e}")
        print(f"Content (truncated): {response.content[:500]}")
        return response.content.decode('utf-8')
    except (gzip.BadGzipFile, zlib.error) as e:
        print(f"DecompressionError: {e}")
        print(f"Content (truncated): {response.content[:100]}")
        return response.content.decode('utf-8')
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        print(f"Decoded content (truncated): {response.content[:100]}")
        return response.content.decode('utf-8')
    except Exception as e:
        print(f"Unexpected error: {e}")
        print(f"Content (truncated): {response.content[:100]}")
        return response.content.decode('utf-8')
    pass

from flask import render_template, send_file, url_for, request

@app.route('/generate_cc', methods=['POST'])
def generate_cc():
    bin_number = request.form['binNumber']
    result = step3(bin_number)
    results = []
    for i in range(0, 3):
        result = step3(bin_number)
        results.append(result)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'VALID_CC.txt')

    with open(file_path, 'w') as f:
        for result in results:
            f.write(result + '\n')  # write the entire result to the file

    return redirect(url_for('download_file'))  # redirect to download file page

@app.route('/download_file')
def download_file():
    return render_template('download_file.html', filename='VALID_CC.txt')

@app.route('/download_file/<filename>')
def download(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)