# import requests
import requests

news_url = "https://economictimes.indiatimes.com/news"
url = requests.get(news_url)
print(url.status_code)
print(url.headers)
# print(url.text)
# url.json()