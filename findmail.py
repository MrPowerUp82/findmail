import re
import requests
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Accept":"*/*"
}
url=input("Url-> ")
page=requests.get(url, headers=headers)
pd=re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+',page.text)
print(pd)