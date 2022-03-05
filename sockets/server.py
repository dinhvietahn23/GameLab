import socket
from _thread import *
import pickle
from game import Game


class Server:
    def __init__(self):
        self.g = Game()
        self.games = {}
        self.server = self.get_ipv4()
        self.port = 5555
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sk.bind((self.server, self.port))
            self.sk.listen(2)
            print("Server started, waiting for a connection")
            print(self.server)
        except socket.error as e:
            str(e)

    def get_ipv4(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address

    def thread_client(self, connect):
        connect.send(str.encode("white"))
        while True:
            try:
                data = connect.recv(4096).decode()
                if not data:
                    print("Disconnected")
                    break
                elif data != "s":
                    x = data.split(",")
                    p = self.g.board.get_piece_at(int(x[1]), int(x[0]))
                    self.g.board.move_piece_to(p, int(x[2]), int(x[3]))
                    #self.g.board.player_turn = "b" if self.g.board.player_turn == "w" else "w"
                    print(p.get_information())
                    print("Received: ", data)
                    print("Sending: ", data)

                connect.sendall(pickle.dumps(self.g))
            except:
                break
        print("Lost connection")
        connect.close()

    def run_new_thread_client(self):
        while True:
            connect, address = self.sk.accept()
            print("Connected to:", address)
            start_new_thread(self.thread_client, (connect,))


s = Server()
s.run_new_thread_client()

