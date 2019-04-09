import sys
import traceback


class Log(object):
    """Stupid logger that writes messages to stdout or stderr accordingly."""

    ERROR = 30
    INFO = 20
    DEBUG = 10
    level = ERROR

    @staticmethod
    def debug(msg, indent=0):
        if Log.level <= 10:
            sys.stdout.write(Log.indent_string(msg, indent) + "\n")

    @staticmethod
    def info(msg, indent=0):
        if Log.level <= 20:
            sys.stdout.write(Log.indent_string(msg, indent) + "\n")

    @staticmethod
    def error(msg, indent=0):
        sys.stderr.write(Log.indent_string(msg, indent) + "\n")
        if Log.level <= 10:
            traceback.print_exc(5)

    @staticmethod
    def indent_string(string, indent):
        if indent > 0:
            return '\n'.join([' ' * indent + l for l in string.splitlines()])
        else:
            return string
