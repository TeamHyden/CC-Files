import requests
import json

urls = [
    'https://api.proxyscrape.com/v4/free-proxy-list/get',
    'https://proxylist.geonode.com/api/proxy-list'
]

# The URL to test the proxies
test_url = 'https://httpbin.org/get'  # A simple URL to test proxy functionality
working_proxies = []

for i in range(len(urls)):
   
    if i == 0: 
        headers = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
        }
        params = {
            'request': 'get_proxies',
            'skip': '0',
            'proxy_format': 'protocolipport',
            'format': 'json',
            'limit': '100',
            'timeout': '20000',
        }

        response = requests.get(urls[i], params=params, headers=headers)
        data = json.loads(response.text)
        try:
            for proxy in data['proxies']:
                protocol = proxy['protocol']
                ip = proxy['ip']
                port = proxy['port']

                # Only test SOCKS4 proxies
                if protocol == 'socks4':
                    proxy_string = f"{protocol}://{ip}:{port}"

                    try:
                        # Test the proxy by sending a GET request
                        proxy_dict = {protocol: proxy_string}
                        test_response = requests.get(test_url, proxies=proxy_dict, timeout=5)

                        # Check if the status code is 200
                        if test_response.status_code == 200:
                            working_proxies.append(proxy_string)
                            print(f"Working proxy found: {proxy_string}")
                            with open('working_proxies.txt', 'a') as f:
                                f.write(f"{proxy_string}\n")

                    except requests.RequestException:
                        print(f"Proxy failed: {proxy_string}")
        except Exception as e:
            print('exception occurs')                        
            continue 


    elif i == 0:
        with open('worked_Proxy.txt', 'a') as f:
            f.write('i am inside 2nd site proxy\n')
        
        params = {
            'google': 'false',
            'limit': '100',
            'page': '1',
            'sort_by': 'lastChecked',
            'sort_type': 'desc',
        }
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'
        }

        response = requests.get(urls[1], headers=headers, params=params)
        
        # Load the response data
        data = json.loads(response.text)

        # Check if 'data' exists in the response
        if 'data' in data:
            print(data)

            for proxy in data['data']:
                country_code = proxy['country']
                port = proxy['port']
                protocols = proxy['protocols']  # This is now a list
                ip = proxy['ip']

                for protocol in protocols:
                    if protocol == 'socks5':
                        proxy_url = f"{protocol}://{ip}:{port}"
                        proxies = {"http": proxy_url, "https": proxy_url}
                        try:
                            test_response = requests.get(test_url, proxies=proxies, timeout=10)
                            if test_response.status_code == 200:
                                with open('worked_Proxy.txt', 'a') as f:
                                    f.write(f"{proxy_url}\n")
                                print(f"Working SOCKS5 proxy found: {proxy_url}")
                        except requests.RequestException:
                            print(f"Proxy failed: {proxy_url}")
    