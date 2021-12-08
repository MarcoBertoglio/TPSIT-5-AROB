import socket as sck

def calcola(stringa):
    for k in stringa:
        if k != "0" and k != "1" and k != "2" and k != "3" and k != "4" and k != "5" and k != "6" and k != "7" and k != "8" and k != "9" and k != "+" and k != "-" and k != "*" and k != "/" and k != "(" and k != ")":
            stringa = stringa.replace(k, "")
    
    return str(eval(stringa))

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(('localhost', 8000))

    while True:
        data = s.recv(4096).decode()

        if data == "exit":
            break

        s.sendall(calcola(data).encode())

    s.close()

main()