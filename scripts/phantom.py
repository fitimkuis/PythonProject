import subprocess

url = "http://www.google.com"
args = ["C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/phantom/phantomjs-2.1.1-windows/bin/phantomjs.exe", "C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/scripts/entire_page.js", url, "--ignore-ssl-errors=true"]

#command = "C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/phantom/phantomjs-2.1.1-windows/bin/phantomjs.exe --ignore-ssl-errors=true C:/Users/TimoK1/testing/robot-e-commerce/resources/scripts/entire_page.js"
process = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE)

# make sure phantomjs has time to download/process the page
# but if we get nothing after 30 sec, just move on
try:
    output, errors = process.communicate(timeout=30)
except Exception as e:
    print("\t\tException: %s" % e)
    process.kill()

# output will be weird, decode to utf-8 to save heartache
phantom_output = ''
for out_line in output.splitlines():
    phantom_output += out_line.decode('utf-8')

print(phantom_output)