import socket as sck
import threading as thr


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    s.bind(('localhost', 5000))
    client = {}


    while True:
        messaggio, indirizzo= s.recvfrom(4096)
        messaggio=messaggio.decode()
        print(messaggio)
        messaggio=messaggio.split(':')

        if messaggio[0]=="nickname":    #se è uguale a nickname èla prima volta che si collega e si salva
                                        #il nome del client e il suo IP
            client[messaggio[1]]= indirizzo
            s.sendto("ok".encode(), client[messaggio[1]])   #manda il messaggio ok per confermare la registrazione
        elif messaggio[1] == "!list":   #richiede la lista di cliente connessi in quel momento
            s.sendto(f"lista:{client.keys()}".encode, indirizzo)
        
        else:
            #controlla che il nickname sia dentro al dizionario se c'è lo manda
            for k in client.keys():
                if k==messaggio[1]:
                    s.sendto(f"{messaggio[1]}:{messaggio[2]}".encode(),client[k])

main()