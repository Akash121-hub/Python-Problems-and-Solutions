import requests
print(requests.__version__)

import requests
res = requests.get('https://google.com/')
print("Response of https://google.com/:")
print(res.status_code)