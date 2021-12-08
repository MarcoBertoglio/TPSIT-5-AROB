import logging
import socket
import threading as thr
import time

registered = False
nickname = ""
SERVER=('192.168.0.122', 5000)

#classe che riceve i messaggi inviati dagli altri utenti
class Receiver(thr.Thread):
    def __init__(self, s): 
        thr.Thread.__init__(self)
        self.running = True 
        self.s = s

    def stop_run(self):
        self.running = False

    def run(self):
        global registered

        while self.running:
            data = self.s.recv(4096).decode()
            
            #se riceve ok la connessione è stata effettuata 
            if data == "OK":
                registered = True
                logging.info(f"\nConnessione avvenuta, registrato. Entrando nella chat mode...")
            
            #se no printa il messaggio ricevuto
            else:
                print(f"\n{data}")

def main():
    global registered
    global nickname
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER)

    ricev = Receiver(s)
    ricev.start()

    while True:
        time.sleep(0.2)

        #se non è ancora registrato lo registra se no si inviano i messaggi agli altri utenti
        if not registered:
            nickname = input("Inserisci un nickname >>>")

            mex = "Nickname:" + nickname
            registered = True

        else:
            destinatario = input("Inserisci il destinatario >>>")

            text = input("Inserisci il messaggio >>>")
            mex = nickname + ":" + destinatario + ":" + text

        s.sendall(mex.encode())

        #se riceve exit chiude la connessione
        if 'exit' in mex.split(":"):
            ricev.stop_run()
            logging.info("Disconnessione...")
            break

    ricev.join()    #chiude il thread
    s.close()

if __name__ == "__main__":
    main()