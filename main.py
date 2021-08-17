from mcapi import *
from org.bukkit.event.player import AsyncPlayerChatEvent
import socket
import threading
PORT = 5050
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
server_address = (SERVER, 5050)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!desconectar"

clients = [] # The clients we have connected to
clients_lock = threading.Lock()

sock.bind(server_address)

def chat(m):
    msg = m.getMessage()
    au = m.getPlayer()
    print(msg)
    print(au)
    clients[0].send(msg.encode(FORMAT))
    clients[0].send(au.getPlayerListName().encode(FORMAT))

def start():
    global ADDR
    sock.listen(1)
    
    
    while True:
        conn, ADDR = sock.accept()
        with clients_lock:
          clients.append(conn)
          print(type(clients))
          print(clients)


x1 = threading.Thread(target=start)
x1.start()
listener = add_event_listener(AsyncPlayerChatEvent, chat)