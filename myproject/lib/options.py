from argparse import ArgumentParser
import platform


class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):

        # overrides usage that is by default something like:
        # usage: PROG [-h] [--foo [FOO]] bar [bar ...]
        # and make path different for Linux and Windows
        usage = None
        if platform.system() == 'Linux':
            usage = './bin/project'
        elif platform.system() == 'Windows':
            usage = '.\\bin\project.bat'

        self.parser = ArgumentParser(usage=usage)

        # inits the argparser with an argument 'test' with
        # a default value 'test-value'
        self.parser.add_argument('-t', # short option
                                 '--test', # full option
                                 default='test-value', # specifies default value for the parameter
                                 dest='test', # determines the name of the attribute that parse_args yields
                                 help='An test option') # specifies help message
        self.parser.add_argument('-s', # short option
                                 '--sample', # full option
                                 dest='sample', # determines the name of the attribute that parse_args yields
                                 help='A sample option') # specifies help message

    def parse(self, args=None):

        # parse known args, returns a Namespace object
        # unknown args are ignored
        # Parse known args returns (Namespace_of_known, list_of_unknown)
        self.known, self.unknown = self.parser.parse_known_args(args)[:]
        if len(self.unknown) != 0:
            print ('*WARN* Unknown args received: ' + repr(self.unknown))