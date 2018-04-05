import requests
import bs4

url = 'http://machine-admin.kadawo.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
tony = requests.get(url, headers=headers)
di = {'name': 'hah', 'age': '26'}
tony2 = requests.post(url, params=di, headers=headers)
# tony2 = requests.post(url, headers=headers)

# print(tony)
# print(tony2)
# print(tony.url)
# print(tony2.url)
# # print(tony.text)
# print(tony.status_code)
# print(tony2.status_code)
# print(tony.raise_for_status())
# print(tony2.raise_for_status())

print(tony.headers)
print(tony.headers)
print(tony.cookies)
print(tony.text)
