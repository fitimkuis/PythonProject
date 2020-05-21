import subprocess

def execute_pabot_runner(comm, args):
    print(comm)
    print(args)
    raw_command = r"{}".format(comm)
    subprocess.call([raw_command]+args)
    #subprocess.call([r'C:\Users\fitim\IdeaProjects\PythonProject\PythonProject\pabotRunnerTest\pabotRunner.bat'])