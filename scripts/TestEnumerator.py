from robot.libraries.BuiltIn import BuiltIn
import logging

from robot.output import librarylogger
from robot.running.context import EXECUTION_CONTEXTS
from robot.api import logger

class TestEnumerator(object):
    ROBOT_LISTENER_API_VERSION = 3
    def __init__(self):
        self.counter = 0

    def start_test(self, data, result):
        self.counter += 1
        result.name = f'{self.counter}. {result.name}'
        logger.info(f'{self.counter}. {result.name}')