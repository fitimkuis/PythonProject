from robot.libraries.BuiltIn import BuiltIn
class ResultModifier(object):
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, max_seconds=10):
        self.max_milliseconds = float(max_seconds) * 1000
        #self.arg = "Keyword added by listener!"
        #self.counter = 0
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

    def log_message(self, msg):
        msg.message = '<b style="font-size: 1.5em">%s</b>' % msg.message
        if msg.level == 'WARN' and not msg.html:
            msg.message = '<b style="font-size: 1.5em">%s</b>' % msg.message
            msg.html = True

    def start_test(self,test, result):
        test.keywords.create(name='Log To Console', args=[self.increment_counter()])

    def increment_counter(self):
        testname = BuiltIn().get_variable_value("${TEST NAME}")
        with open("counter.txt", 'r') as f:
            for line in f:
                line = line.rstrip()
                if not line or len(line) == 0:
                    break
                else:
                    line = int(line) + 1
                    ret = self.write_counter(line)
                    return str(ret)+". "+testname

    def write_counter(self, cont):
        with open("counter.txt", 'w') as fw:
            print(cont)
            fw.write(str(cont))
            return cont


