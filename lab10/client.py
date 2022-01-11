import Pyro4

msg = input("[client] Send message =")
server = Pyro4.Proxy("PYRONAME:my_server")
print(server.message(msg))
