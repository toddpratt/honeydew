
from twisted.protocols import basic

class LineProto(basic.LineReceiver):

    def lineReceived(self, line):
        """Receives a raw line."""


        # TODO: process a line and dispatch to command handlers
        #
        # The line needs to be split into words (shlex module).  The first word
        # is the command and the rest are arguments.

        self.sendLine(line)  # just echo the line back for initial test
