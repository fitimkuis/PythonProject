#pabot --processes 3   --outputdir c:\pabot-demo\reports\    *.txt

import subprocess

def execute_pabot():
    subprocess.call([r'C:\Users\fitim\IdeaProjects\PythonProject\PythonProject\scripts\run_pabot.bat'])

def execute_rebot():
    subprocess.call([r'C:\Users\fitim\IdeaProjects\PythonProject\PythonProject\scripts\run_rebot.bat'])


#execute_pabot()