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
    selected_value = request.json['selectedValue']  # Get the selected value from the AJAX request
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('')  # create an empty file
    # Call the step1 and step2 functions
    randomnumbers = []
    def step1():
        def generate_random_number():
             while True:
                num = random.randint(10000, 99999)
                num_str = str(num)
                # Check if any digit repeats
                if any(num_str.count(digit) > 1 for digit in num_str):
                    return int(selected_value + num_str)
                            # Use the selected_value here
                    
        for _ in range(30):
            randomnumbers.append(generate_random_number())

    def step2(bin):   
        api_key = 'a3eb03197f38fbed025a8c195d48c891b7d2a5fc'
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
from datetime import datetime, timedelta

import random
from datetime import datetime, timedelta

def step3(bin):
    # Generate a random year
    prefix = bin
    remaining_digits = "".join([str(random.randint(0, 9)) for _ in range(10)])  # Changed 10 to 9 for valid digits
    random_number = prefix + remaining_digits

    # Generate a random month
    random_month = random.randint(1, 12)
    formatted_month = str(random_month).zfill(2)  # Ensures month is in "MM" format

    # Generate a random year between 2024 and 2035
    random_year = random.randint(2024, 2035)

    # Generate a random 3-digit number
    random_3_digit = str(random.randint(0, 999)).zfill(3)

    # Combine the results into the required format
    result = f"{random_number}|{formatted_month}|{random_year}|{random_3_digit}"
    return result




def step4():

    for result2 in results:    
        value = result2.strip().split("|")[0]  # Extract the credit card number
        cc_validity(value, result)  # Call the inner function to validate
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
            response = requests.get(f'https://dnschecker.org/ajax_files/gen_csrf.php?upd=239.{random_number}', headers=headers)
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
                print(Fore.GREEN + "Valid number" + Fore.RESET)
                with open('LiveCC.txt', 'a') as f:
                    f.write(f'{full_cc} \n')
        except requests.exceptions.RequestException as e:
            print('Error making request:', e)

    # Gather results from valid bins
    results = []
    for bin in valid_bin:  # Assumes valid_bin is populated elsewhere in your code
        result = step3(bin)  # Generate credit card information
        results.append(result)


    step4(results)


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
    for i in range(0, 200):
        result = step3(bin_number)
        results.append(result)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'VALID_CC.txt')

    with open(file_path, 'w') as f:
        for result in results:
            f.write(result)  # write the entire result to the file
            f.write("\n")

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