from thespian.actors import *


class Hello(Actor):
    def receiveMessage(self, message, sender):
        print('[hello] message =%s' % message)
        self.send(sender, "Hello from Hello!")


if __name__ == "__main__":
    hello = ActorSystem().createActor(Hello)
    print("[system] msg=%s" % ActorSystem().ask(hello, "hi", 1))
    ActorSystem().tell(hello, ActorExitRequest())
