import socket as sck
import threading as thr
import sqlite3

class Classe_Thread(thr.Thread):
    def __init__(self, connessione, indirizzo, nome, operazioni):
        thr.Thread.__init__(self)   
        self.connessione = connessione
        self.indirizzo = indirizzo
        self.nome = nome
        self.operazioni = operazioni
        self.running = True

    
    def run(self):
        for k in self.operazioni:
            if self.nome == k[1]:
                self.connessione.sendall(k[2].encode())
                risultato = self.connessione.recv(4096).decode()
                print(f"{k[2]} = {risultato} from {self.indirizzo[0]} - {self.indirizzo[1]}")
        
        self.connessione.sendall("exit".encode())
        
            


def main():
    #socket
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind(('localhost', 8000))
    s.listen()

    #creazione del database e interrogazione
    database = sqlite3.connect('operations.db')
    cursore = database.cursor()
    operazioni = cursore.execute("SELECT * FROM operations").fetchall()

    #calcolo del numero di client da utilizzare
    numero_client = []
    for k in operazioni:
        if k[1] not in numero_client:
            numero_client.append(k[1])

    #creazione e avvio dei threads
    threads = {}
    for k in numero_client:
        connessione, indrizzo = s.accept()

        threads[k] = Classe_Thread(connessione, indrizzo, k, operazioni)
        threads[k].start()
    
    
    database.close()

main()