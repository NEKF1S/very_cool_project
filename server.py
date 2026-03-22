import socket
import threading

HOST = "0.0.0.0"
PORT = 4
clients = []
names = {}
lock = threading.Lock()

def broadcast(text: str):
    with lock:
        dead = []
        for c in clients:
            try:
                c.send(text.encode())
            except:
                dead.append(c)
        for c in dead:
            try:
                c.close()
            except:
                pass
            if c in clients:
                clients.remove(c)
            names.pop(c)


def handle_client(conn):
    try:
        conn.send("Введіть ім'я: ".encode())
        name = conn.recv(1024).decode().strip()
        if not name:
            name = "Anonymous"
        with lock:
            clients.append(conn)
            names[conn] = name
        broadcast(f"\n✅ {name} приєднався до чату!\n")
        while True:
            msg = conn.recv(1024)
            if not msg:
                break
            text = msg.decode().strip()
            if not text:
                continue
            if text.lower() in ["/exit", "/quit"]:
                break
            broadcast(f"{name}: {text}\n")
    except:
        pass
    finally:
        with lock:
            if conn in clients:
                clients.remove(conn)
            left_name = names.pop(conn, None)
        try:
            conn.close()
        except:
            pass
        if left_name:
            broadcast(f"\n🚪 {left_name} вийшов з чату.\n")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    print(f"Server started on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(conn,))
        t.start()

main()