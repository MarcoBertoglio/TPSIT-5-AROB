'''implementare una chat tra la nostra classe, chat UDP. gli utenti devono essere identificati
ci sarà un server con all'interno una tabella dove dentro ci saranno i nickname e gli ip.
il client manda un messaggio al server e il server quando riceve il messaggio conosce anche l'ip,
una volta ricevuto il server rispode ok.
hello = f"NICKNAME: {nick_name}"
ok = "ok"

'''
import socket as sck
import threading as thr

s1 = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

s1.sendto(("nick_name:" + input("inserisci un nick_name: ")).encode(), ("192.168.0.124", 8000))

while True:
    dato, indirizzo = s1.recvfrom(4096)

    print(dato.decode())

    s1.close()

    break