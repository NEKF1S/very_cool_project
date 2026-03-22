import socket
import threading

HOST = "192.168.0.223"
PORT = 6


def receive_messages(sock: socket.socket):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Відключено від сервера.")
                break
            print(data.decode(), end="")
        except:
            break


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    t = threading.Thread(target=receive_messages, args=(sock,), daemon=True)
    t.start()
    while True:
        text = input()
        sock.send(text.encode("utf-8"))

        if text.lower() in ["/exit", "/quit"]:
            break
    sock.close()


main()