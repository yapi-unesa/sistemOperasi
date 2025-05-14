import socket
import threading


HEADER = 64
PORT = 5050
SERVER = "10.59.101.89"
ADDR = (SERVER, PORT)
FORMAT = "UTF-8"
pesan_terputus="terputus!!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 dan tcp
server.bind(ADDR) 


def handle_client(conn, addr):
  print("[koneksi] {addr} connected.")

  connected = True
  while connected:
    msg_length=conn.recv(HEADER).decode(FORMAT)
    if msg_length:
      msg_length= int(msg_length)
      msg = conn.recv(msg_length).decode(FORMAT)
      if msg == pesan_terputus:
        connected = False

      print("[{addr}] {msg}")

  conn.close()
    
def start():
  server.listen()
  print("[LISTENING] server is listening on {SERVER}")
  while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print("[AKTIF] {threading.active_count() - 1 }")

print("[STARTING] server is starting...")
start()









