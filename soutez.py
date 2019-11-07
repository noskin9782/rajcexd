import requests
import random
import string
import random
import time
from proxy_requests import ProxyRequests



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.71'
}

while True:
    cas = random.randint(0,500)
    #from proxy_requests import ProxyRequests
    #register_data = {"POST":"/vote/479 HTTP/1.1"}
    #print (register_data)
    #url = 'https://souteze.rajce.net/vote/479'
    #r = s.post(url, json=register_data, headers=headers, proxies = proxies)
    #print(r.content)
    r = ProxyRequests("https://souteze.rajce.net/vote/504")
    r.post({"POST":"/vote/504 HTTP/1.1"})
    print(r)
    print(r.get_status_code())
    print(r.get_proxy_used())
    #time.sleep(cas)
