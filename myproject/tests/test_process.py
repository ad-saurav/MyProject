import unittest

from myproject.lib import Process, ProcessException


class TestProcess(unittest.TestCase):

    def setUp(self):
        self.process = Process()

    def test_should_execute_successfully(self):
        self.assertEquals(self.process.execute("echo test").decode().rstrip('\n'), "test")

    def test_should_raise_exception_on_failed_execution(self):
        self.assertRaises(ProcessException,
                          self.process.execute,
                          "sh -c 'return 1'")


if __name__ == '__main__':
    unittest.main()