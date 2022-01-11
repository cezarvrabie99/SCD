import Pyro4
import Pyro4.naming
import shop

ns = Pyro4.naming.locateNS()
daemon = Pyro4.core.Daemon()
uri = daemon.register(shop.Shop())
ns.register("lab_10.Shop".uri)
print(list(ns.list(prefix="lab_10").keys()))
daemon.requestLoop()
