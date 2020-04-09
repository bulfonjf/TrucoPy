from network import Network
import socket
from _thread import start_new_thread
import signal
import threading
import sys

def signal_handler(signal, frame):
    print("exiting")
    sys.exit(0)

def threaded_client():
    print("comienza el cliente")
    print("creo la clase network...")
    n = Network()
    print("me conecto...")
    n.connect()
    print("conectado")
    run = True
    while run:
        try:
            print("manda el chat que quieras")
            chat = input()
            if(chat == "quit"):
                run = False
            else:
                print("ahora desde el cliente mando un msj")
                msjRecibido = n.send(chat)
                print("se envio", chat)
                print("msj que recibi desde el server", msjRecibido.decode())
        except Exception as err:
            print("Error en cliente linea 13", err)
            run = False

def main():
    signal.signal(signal.SIGINT, signal_handler)
    threads_arr = []
    t = threading.Thread(target=threaded_client, args=())
    threads_arr.append(t)
    t.daemon = True # die when the main thread dies
    t.start()
    for thr in threads_arr: # let them all start before joining
        thr.join()


main()