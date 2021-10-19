from robot.libraries.BuiltIn import BuiltIn
import logging

from robot.output import librarylogger
from robot.running.context import EXECUTION_CONTEXTS


class ResultModifier(object):
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, max_seconds=10):
        self.max_milliseconds = float(max_seconds) * 1000
        #self.arg = "Keyword added by listener!"
        self.counter = 0
        with open("counter.txt", 'w') as fw:
            fw.write('0')

    def start_suite(self, data, suite):
        suite.doc = 'Documentation set by listener.'
        # Information about tests only available via data at this point.
        smoke_tests = [test for test in data.tests if 'smoke' in test.tags]
        suite.metadata['Smoke tests'] = len(smoke_tests)

    def end_test(self, data, test):
        if test.status == 'PASS' and test.elapsedtime > self.max_milliseconds:
            test.status = 'FAIL'
            test.message = 'Test execution took too long.'
    '''
    def log_message(self, msg):
        msg.message = '<b style="font-size: 1.5em">%s</b>' % msg.message
        if msg.level == 'WARN' and not msg.html:
            msg.message = '<b style="font-size: 1.5em">%s</b>' % msg.message
            msg.html = True'''

    def start_test(self,test, result):
        from robot.api import logger
        self.counter = self.counter + 1
        #test.keywords.create(name='Log To Console', args=[self.add_counter(test)])
        #test.keywords.create(name='Log To Console', args=[self.info(test.name)])
        self.info(test.name)
        self.my_keyword(str(self.counter)+". "+test.name)
        logger.info(str(self.counter)+". "+test.name, html=True)

    def my_keyword(self, arg):
        from robot.api import logger
        logger.debug('Got argument %s.' % arg)
        #do_something()
        logger.info('<i>This</i> is a boring example.', html=True)

    def add_counter(self, test):
        self.counter = self.counter + 1
        return str(self.counter)+". "+test.name

    def console(self, msg, newline=True, stream='stdout'):
        """Writes the message to the console.

        If the ``newline`` argument is ``True``, a newline character is
        automatically added to the message.

        By default the message is written to the standard output stream.
        Using the standard error stream is possibly by giving the ``stream``
        argument value ``'stderr'``. This is a new feature in RF 2.8.2.
        """
        librarylogger.console(msg, newline, stream)
        return msg

    def info(self, msg, html=True, also_console=True):
        """Writes the message to the log file using the ``INFO`` level.

        If ``also_console`` argument is set to ``True``, the message is
        written both to the log file and to the console.
        """
        from robot.api import logger
        #self.counter = self.counter + 1
        #logger = logging.getLogger("RobotFramework")
        logger.write(str(self.counter)+". "+msg, 'INFO')
        #logger.debug('INFO', str(self.counter)+". "+msg)
        #librarylogger.write(str(self.counter)+". "+msg, 'INFO', html)
        #mess = self.write(str(self.counter)+". "+msg, 'INFO', html)
        if also_console:
            self.console(str(self.counter)+". "+msg)
        #return str(self.counter)+". "+msg

    def write(self, msg, level='INFO', html=True):
        """Writes the message to the log file using the given level.

        Valid log levels are ``TRACE``, ``DEBUG``, ``INFO`` (default since RF
        2.9.1), ``WARN``, and ``ERROR`` (new in RF 2.9). Additionally it is
        possible to use ``HTML`` pseudo log level that logs the message as HTML
        using the ``INFO`` level.

        Instead of using this method, it is generally better to use the level
        specific methods such as ``info`` and ``debug`` that have separate
        ``html`` argument to control the message format.
        """

        if EXECUTION_CONTEXTS.current is not None:
            librarylogger.write(msg, level, html)
        #else:
        logger = logging.getLogger("RobotFramework")
        '''
            level = {'TRACE': logging.DEBUG // 2,
                     'DEBUG': logging.DEBUG,
                     'INFO': logging.INFO,
                     'HTML': logging.INFO,
                     'WARN': logging.WARN,
                     'ERROR': logging.ERROR}[level]
        '''
        logger.log(level, msg)
        return msg

    def increment_counter(self, test):
        testname = BuiltIn().get_variable_value("${TEST NAME}")
        with open("counter.txt", 'r') as f:
            for line in f:
                line = line.rstrip()
                if not line or len(line) == 0:
                    break
                else:
                    line = int(line) + 1
                    ret = self.write_counter(line)
                    return str(ret)+". "+test.name

    def write_counter(self, cont):
        with open("counter.txt", 'w') as fw:
            print(cont)
            fw.write(str(cont))
            return cont