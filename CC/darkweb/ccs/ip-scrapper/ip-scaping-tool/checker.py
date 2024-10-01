import requests
import socks

proxies = {'https': 'socks4://13.237.182.217:3128'}

# Create a SOCKS4 connection
socks.set_default_proxy(socks.SOCKS4, '136.226.255.23', 10999)

# Make the request
response = requests.get("https://api.ipify.org/", timeout=20, verify=True)

if response.status_code == 200:
    print('all set')
    my_ip = response.text.strip()
    print(my_ip)
