import subprocess

def execute_entire_suite(command, args):
    print(args)
    #subprocess.call([r'C:\Users\fitim\IdeaProjects\PythonProject\PythonProject\scripts\entire_suite.bat'])
    raw_command = r"{}".format(command)
    subprocess.call([raw_command]+args)