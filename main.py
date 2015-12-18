import linerecv

from twisted.internet import reactor
from twisted.internet import protocol

if __name__ == "__main__":
    sf = protocol.ServerFactory()
    sf.protocol = linerecv.LineProto
    reactor.listen(8023, sf)
