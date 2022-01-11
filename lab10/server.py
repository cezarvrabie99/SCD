import Pyro4


@Pyro4.expose
class Server(object):
    def message(self, name):
        return ("[server]Hello from " + str(name))


def startServer():
    server = Server()
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(server)
    ns.register("my_server", uri)
    print("Server Ready at uri=", uri)
    daemon.requestLoop()


if __name__ == "__main__":
    startServer()
