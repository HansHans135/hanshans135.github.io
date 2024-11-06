import requests
r=requests.post("https://www.dcard.tw/service/api/v2/posts")
print(r.text)