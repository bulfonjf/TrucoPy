import socket
from _thread import start_new_thread
import signal
import threading
import sys

def signal_handler(signal, frame):
    print("exiting")
    sys.exit(0)


server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

contador = 0

def threaded_server(conn, idPlayer):
    print("server manda al que se acaba de conectar su Id de player")
    conn.send(str.encode(str(idPlayer)))

    while True:
        try:
            print("recibiendo data...")
            data = conn.recv(4096).decode()
            if not data:
                print("data es nulo")
                break
            else:
                print("", data)
                print("enviando msj...")
                conn.sendall(str.encode(data))
                print("enviado")
        except Exception as err:
            print("", err)
            break

    print("Lost connection")

    try:
        print("Closing Game")
    except Exception as err:
        print("Server error line 53, error:", err)
        pass
    finally:
        if(idPlayer in connected): print("jugador {} va a ser removido".format(idPlayer))
        connected.remove(idPlayer)
        if(idPlayer in connected): print("jugador {} NO se quito".format(idPlayer))
        else: print("jugador {} fue removido".format(idPlayer))
        print("jugadores restantes", len(connected))
        print("Closing connection")
        conn.close()


run = True
while run:
    try:
        global connected
        connected = set()
        contador += 1
        print("contador", contador)
        if(not any(connected)): print("nadie conectado")
        conn, addr = s.accept()
        print("Connected to:", addr)
        connected.add(addr)

        signal.signal(signal.SIGINT, signal_handler)
        threads_arr = []
        t = threading.Thread(target=threaded_server, args=(conn, addr))
        threads_arr.append(t)
        t.daemon = True # die when the main thread dies
        t.start()
        for thr in threads_arr: # let them all start before joining
            thr.join()
        
        print("server line 66 termino el codigo del new thread")
    except Exception as err:
        print("Server error line 65, error:", err)
        pass
    finally:
        print("not any connected", not any(connected))
        if(not any(connected) and contador >= 2):
            run = False
        else:
            run = True

