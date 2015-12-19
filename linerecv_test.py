
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

    def testLineReceived(self):
        cmd = MockCommand()
        lp = linerecv.LineProto()
        lp.factory = MockFactory({'cmd': cmd})
        lp.lineReceived(' cmd argument ')
        self.assertEqual(cmd.args, ['cmd', 'argument'])


if __name__ == '__main__':
    unittest.main()

