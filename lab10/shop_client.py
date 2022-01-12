import sys
import Pyro4
import Pyro4.naming


class client(object):
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def doShopping_deposit_cash(self, Shop):
        print("\n*** %s is doing shopping with %s:" \
              % (self.name, Shop.name()))
        print("Log on")
        Shop.logOn(self.name)
        print("Deposit money %s" % self.cash)
        Shop.deposit(self.name, self.cash)
        print("Balance=%.2f" % Shop.balance(self.name))
        print("Deposit money %s" % self.cash)
        Shop.deposit(self.name, 50)
        print("Balance=%.2f" % Shop.balance(self.name))
        print("Log out")
        Shop.logOut(self.name)

    def doShopping_buy_book(self, Shop):
        print("\n*** %s is doing shopping with %s:" \
              % (self.name, Shop.name()))
        print("Log on")
        Shop.logOn(self.name)
        print("Deposit money %s" % self.cash)
        Shop.deposit(self.name, self.cash)
        print("Balance=%.2f" % Shop.balance(self.name))
        print("%s is buying a book for %s$" \
              % (self.name, 37))
        Shop.buy(self.name, 37)
        print("Log out")
        Shop.logOut(self.name)


if __name__ == '__main__':
    ns = Pyro4.naming.locateNS()
    uri = ns.lookup("lab_10.Shop")
    print(uri)
    Shop = Pyro4.core.Proxy(uri)
    c1 = client('Popescu', 50)
    c2 = client('Ionescu', 50)
    c2.doShopping_buy_book(Shop)
    c1.doShopping_deposit_cash(Shop)
    print("\nThe accounts in the %s:" % Shop.name())
    accounts = Shop.allAccounts()
    for name in accounts.keys():
        print(" %s :%.2f " % (name, accounts[name]))
