#!/usr/bin/python

import re
import sys

class Task:
    ''' Object representing an tcs-bank task '''

    def __init__(self, task_name, duration):
        self.name = task_name
        self.durations = [int(duration)]

    def average(self):
        return sum(self.durations)/len(self.durations)

    def __str__(self):
        return self.name + " durations: " + self.durations + ", avg " + str(self.average()) + " ms"

    def __repr__(self):
        return self.name + " durations: " + self.durations + ", avg " + str(self.average()) + " ms"

    def min(self):
            return min(self.durations)

    def __str__(self):
        return self.name + " durations: " + self.durations + ", min " + str(self.min()) + " ms"

    def __repr__(self):
        return self.name + " durations: " + self.durations + ", min " + str(self.min()) + " ms"

    def max(self):
        return max(self.durations)

    def __str__(self):
        return self.name + " durations: " + self.durations + ", max " + str(self.max()) + " ms"

    def __repr__(self):
        return self.name + " durations: " + self.durations + ", max " + str(self.max()) + " ms"


'''
tasks = {}
for line in sys.stdin:
        match = re.match(r'^.*Execution ended for task ([\S\s]+) for ([\S\s]+) * duration ([\d]+)ms.*', line)
        if match is not None:
            task_name = match.groups()[0]
            duration = match.groups()[2]
            #names.append(name)
            if match.groups()[1] is not None:
                task_name = match.groups()[0]+" "+match.groups()[1]

        #print(task_name + " " + duration + " ms")

        task = tasks.get(task_name, None)

        if task is None:
            tasks[task_name] = Task(task_name, duration)
        else:
            task.durations.append(int(duration))

for key, task in tasks.items():
    print(task.name + " avg " + str(task.average()) + " ms"+ " min " + str(task.min()) + " ms"+ " max " + str(task.max()) + " ms")
'''
if __name__ == '__main__':
    log_file = r'C:\Users\timok1\testing\robot-testcases-python3\RobotTesting\com\testing\parse-log\fi-point.log.2020-02-24.txt'
    #for line in sys.stdin:
    tasks = {}
    with open(log_file, "r") as file:
        for line in file:
            #match = re.match(r'^.*Execution ended for task ([\S\s]+) for .* duration ([\d]+)ms.*', line)
            #if match is not None:
            #    task_name = match.groups()[0]
            #    duration = match.groups()[1]
            match = re.match(r'^.*Execution ended for task ([\S\s]+) for ([\S\s]+) * duration ([\d]+)ms.*', line)

            first = ""
            task_name = ""
            duration = 0
            if match is not None:
                first = match.groups()[0]
            if not (first.startswith('XML_REPORT') or first.startswith('ACCOUNT_STATEMENT')):
                if match is not None:
                    task_name = match.groups()[0]
                    duration = match.groups()[2]
                    #names.append(name)
                    if match.groups()[1] is not None:
                        task_name = match.groups()[0]+" "+match.groups()[1]

                #print(task_name + " " + duration + " ms")

                task = tasks.get(task_name, None)

                if task is None:
                    tasks[task_name] = Task(task_name, duration)
                else:
                    task.durations.append(int(duration))

    for key, task in tasks.items():
        print(task.name + " avg " + str(task.average()) + " ms"+ " min " + str(task.min()) + " ms"+ " max " + str(task.max()) + " ms")
