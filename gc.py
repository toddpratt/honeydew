from twisted.internet import reactor
from twisted.internet import threads

import proto
import ui

if __name__ == "__main__":
  app = ui.IrcClient()
  def startUI():
    threads.deferToThread(app.run)

  factory = proto.LineProtoFactory()
  factory.got_line_callback = app.got_line
  factory.connectedCallback = startUI
  factory.disconnectedCallback = app.quit
  app.factory = factory
  reactor.connectTCP('localhost', 9191, factory)

  reactor.run()
