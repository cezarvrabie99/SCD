from thespian.actors import *
import sys


class Greeting(object):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


class Hello(Actor):
    def receiveMessage(self, message, sender):
        if message == "hi":
            greeting = Greeting('Hello')
            world = self.createActor(World)
            punct = self.createActor(Punctuate)
            greeting.nextActors = [punct, sender]
            self.send(world, greeting)


class World(Actor):
    def receiveMessage(self, message, sender):
        if isinstance(message, Greeting):
            message.message = message.message + " World"
            nextActor = message.nextActors[0]
            self.send(nextActor, message)


class Punctuate(Actor):
    def receiveMessage(self, message, sender):
        if isinstance(message, Greeting):
            message.message = message.message + "!"
            nextActor = message.nextActors[1]
            self.send(nextActor, message)


if __name__ == "__main__":
    hello = ActorSystem().createActor(Hello)
    print(ActorSystem().ask(hello, 'hi', 1))
    ActorSystem().tell(hello, ActorExitRequest())
