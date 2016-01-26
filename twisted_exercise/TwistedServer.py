from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class TwistedServer(Protocol):

    def connectionMade(self):
        print 'Got Connection from ', self.transport.client

    def connectionLost(self, reason):
        print self.transport.client, 'disconnected'

    def dataReceived(self, data):
        print data

factory = Factory()
factory.protocol = TwistedServer

reactor.listenTCP(2345, factory)
reactor.run()