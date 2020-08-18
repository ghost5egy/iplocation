import requests , sys , json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ipaddress", help="tareget ip >
args = parser.parse_args()
ipaddr = args.ipaddress
url = 'https://ipapi.co/' + ipaddr + '/json/'
#print(url)
response = requests.get(url)
res = json.loads(response.content.decode('utf-8'))
print(res['ip'])
print(res['country'] + '  ' + res['country_name'])
print(res['region'] + '  ' + res['region_code'])
print(res['city'])
