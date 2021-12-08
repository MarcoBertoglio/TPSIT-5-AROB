import socket
import threading


class Classe_Thread(threading.Thread):
    def __init__(self): 
        threading.Thread.__init__(self)
        self.running = True 

    def run(self):
        while self.running:
            data, indirizzo = s.recvfrom(4096) #ricevo i messaggi che mi inviano
            print(data.decode())


def main():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    nick= input("Inserisci il tuo nickname: ")
    s.sendto((f"nickname:{nick}").encode(), ("192.168.0.126", 5000))  #invia il nick al server

    messaggio, indirizzo= s.recvfrom(4096)  #stampo l'ok di avvenute connessione
    print(messaggio.decode())

    client = Classe_Thread()
    client.start()

    if messaggio.decode()=="ok":    #se ricevo l'ok la chat è attiva e si possono inviare i messaggi
        print("chat mode")
        while True:
            #invio i messaggi a un mio compagno inserendo il suo nick
            messaggio = input()
            s.sendto((f"{nick}:{messaggio}").encode(), ("192.168.0.126", 5000))
        


main()