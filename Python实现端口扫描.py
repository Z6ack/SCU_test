from socket import *
import threading
import scapy.all as s
from IPy import IP as IPY


thread = []


def Scanner(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        print("[open] ports:" + str(port))
    except:
        pass
    s.close()


def ctrl_Scan(host):
    for port in range(1, 8080):
        t = threading.Thread(target=Scanner, args=(host, port))
        thread.append(t)
        t.start()

    for t in thread:
        t.join()


def Ping_icmp(dest):
    print("=" * 100)
    print("\n正在进行为PING扫描：")
    ip_addr = IPY(dest)
    for ip in ip_addr:
        # print(ip)
        packet = s.IP(dst=str(ip)) / s.ICMP() / b'rootkit'
        ping = s.sr1(packet, timeout=1, verbose=False)
        if ping:
            print(str(ip) + "主机已开启")
        else:
            print(str(ip) + "主机未开启")

    print("=" * 100)


def SYN_scan(ip, port):
    print("=" * 100)
    print("\n正在进行为SYN的半连接扫描：")
    p = s.IP(dst=ip) / s.TCP(dport=int(port), flags="S")
    link = s.sr1(p, timeout=1, verbose=1)
    if link[s.TCP].flags == 'SA':
        print("[SYN]The PORT is open.")
    else:
        print("[SYN]The PORT is closed.")
    print(ip, port)
    print("=" * 100)


def ACK_scan(ip, port):
    print("=" * 100)
    print("\n正在进行为ACK的半连接扫描：")
    p = s.IP(dst=ip) / s.TCP(dport=int(port), flags="A")
    link = s.sr1(p, timeout=1, verbose=1)
    if link == None:
        print("[ACK]The host is closed.")
    else:
        if link != None and link.ttl <= 64:
            print("[ACK]The host is open.")
        elif link != None and link.ttl > 64:
            print("[ACK]The host is closed.")
    print(ip, port)
    print("=" * 100)


def FIN_scan(ip, port):
    print("=" * 100)
    print("\n正在进行为FIN的半连接扫描：")
    p = s.IP(dst=ip) / s.TCP(dport=int(port), flags="F")
    link = s.sr1(p, timeout=1, verbose=1)
    if link == None:
        print("[FIN]The PORT is open.")
    elif link != None and link[s.TCP].flags == 'RA':
        link.display()
        print("[FIN]The PORT is closed.")
    print(ip, port)
    print("=" * 100)


def NULL_scan(ip, port):
    print("=" * 100)
    print("\n正在进行为NULL的半连接扫描：")
    p = s.IP(dst=ip) / s.TCP(dport=int(port), flags="")
    link = s.sr1(p, timeout=1, verbose=1)
    if link == None:
        print("[NULL]The PORT is open.")
    elif link != None and link[s.TCP].flags == 'RA':
        link.display()
        print("[NULL]The PORT is closed.")
    print(ip, port)
    print("=" * 100)


def XMAS_scan(ip, port):
    print("=" * 100)
    print("\n正在进行为Xmas的半连接扫描：")
    p = s.IP(dst=ip) / s.TCP(dport=int(port), flags="FPU")
    link = s.sr1(p, timeout=1, verbose=1)
    if link == None:
        print("[Xmas]The PORT is open.")
    elif link != None and link[s.TCP].flags == 'RA':
        link.display()
        print("[Xmas]The PORT is closed.")
    print(ip, port)
    print("=" * 100)


def WINOWS_scan(ip, port):

    print("=" * 100)
    print("\n正在进行为WINDOWS的半连接扫描：")
    p = s.IP(dst=ip) / s.TCP(dport=int(port), flags="A")
    link = s.sr1(p, timeout=1, verbose=1)
    if (str(type(link)) == "<class 'NoneType'>"):
        print("[WINDOWS]The PORT is closed.")
    elif (link.haslayer(s.TCP)):
        if (link.getlayer(s.TCP).window == 0):
            print("[WINDOWS]The PORT is closed.")
        elif (link.getlayer(s.TCP).window > 0):
            print("[WINDOWS]The PORT is OPEN.")
    else:
        print("[WINDOWS]The PORT is closed.")
    print(ip,port)
    print("=" * 100)


if __name__ == '__main__':
    ctrl_Scan()
    Ping_icmp()
    ACK_scan()
    SYN_scan()
    FIN_scan()
    NULL_scan()
    XMAS_scan()
    WINOWS_scan()