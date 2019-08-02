from .process import Process


class Project:

    def __init__(self, options):
        self.options = options
        self.process = Process()

    def date(self):
        return self._get_date()

    def _get_date(self):
        # prints stdout of subprocess with command "date"
        # strips tailing end of lines
        return self.process.execute("date").decode().rstrip('\n')

    def hello(self):
        return self._get_hello()

    def _get_hello(self):
        # prints stdout of subprocess with command "echo hello!"
        # strips tailing end of lines
        return self.process.execute("echo Hello Python!").decode().rstrip('\n')

    def print_test_arg(self):
        return self.options.known