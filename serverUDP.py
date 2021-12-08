import socket as sck
dizionario = {}

s1 = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

s1.bind(('localhost', 8000))

while True:
    dato, indirizzo = s1.recvfrom(4096)
    print(dato.decode())

    s1.sendto("ok".encode(), indirizzo)

    dizionario[dato.decode()] = indirizzo