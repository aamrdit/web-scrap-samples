import requests
import pprint
URL = "https://www.google.com"


# Dictionaryof HTTP headers
headers = {'User-Agent': f'Aamir Butt (aamir.butt@outlook.com)'}
response = requests.get(URL, headers=headers)


print(response.status_code)

pprint.pprint(response.text)

# writing to file

with open('data/google.html', 'w') as file:
    file.write(response.text)
