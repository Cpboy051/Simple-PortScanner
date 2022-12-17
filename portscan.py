import socket
import sys

print("Port Scanner UDP and TCP\n")
target = input("Enter IP or a Host to scan : ")

tcp = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995, 1723, 3306, 3389, 5900, 8080]
udp = [53, 67, 68, 69, 123, 135, 137, 138, 139, 161, 162, 445, 500, 514, 520, 631, 1434, 1900, 4500, 49152]

try:
            for port in tcp + udp:
              s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              socket.setdefaulttimeout(1)
              result = s.connect_ex((target, port))
              if result == 0:
                print(f"Port {port} is open!")
                s.close()


except socket.gaierror:
        print("IP or Hostname not valid!")
        sys.exit()
