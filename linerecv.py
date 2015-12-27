import shlex

from twisted.protocols import basic

class LineProto(basic.LineReceiver):
    """Dispatches commands."""

    def connectionMade(self):
        print 'connection'
        self.sendLine('Welcome.')

    def lineReceived(self, line):
        """Receives a raw line."""
        print line
        args = shlex.split(line)
        command = self.factory.commands.get(args[0])
        if command:
            command.run(args)
        else:
            self.sendLine("%s: command not found" % args[0])
