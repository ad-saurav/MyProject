import sys

from lib import Project
from lib import Options


def run_project(args):
    options = Options()
    options.parse(args[1:])

    project = Project(options)

    print('')
    print('---------------------- Output ----------------------')
    print('')
    print('Printing current date & time: ', project.date())
    print('Printing Hello Python: ', project.hello())
    print('Printing command prompt args: ', project.print_test_arg())
    print('')
    print('------------------------ End -----------------------')


if __name__ == '__main__':
    run_project(sys.argv)