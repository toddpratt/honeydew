from twisted.protocols import basic
from twisted.internet import protocol

class LineProto(basic.LineReceiver):

  def connectionMade(self):
    self.factory.connectedCallback()

  def connectionLost(self, _):
    self.factory.disconnectedCallback()

  def lineReceived(self, line):
    self.factory.gotLine(line)

class LineProtoFactory(protocol.ClientFactory):

  got_line_callback = None

  def gotLine(self, line):
    self.got_line_callback(line)

  def buildProtocol(self, addr):
    self.proto = LineProto()
    self.proto.factory = self
    return self.proto
