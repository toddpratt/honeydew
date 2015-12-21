
import linerecv
import unittest


class MockCommand(object):

    def __init__(self):
        self.args = None

    def run(self, args):
        self.args = args


class MockFactory(object):

    def __init__(self, commands):
        self.commands = commands


class TestLineRecv(unittest.TestCase):

    def setUp(self):
        self.lp = linerecv.LineProto()

    def sendLineMock(self, line):
        self.lineSent = line

    def testLineReceived(self):
        cmd = MockCommand()
        self.lp.factory = MockFactory({'cmd': cmd})
        self.lp.lineReceived(' cmd argument ')
        self.assertEqual(cmd.args, ['cmd', 'argument'])

    def testLineReceivedNoCommand(self):
        self.lp.sendLine = self.sendLineMock
        self.lp.factory = MockFactory({})
        self.lp.lineReceived(' nocmd argument '),
        self.assertEqual(self.lineSent, "nocmd: command not found")


if __name__ == '__main__':
    unittest.main()

