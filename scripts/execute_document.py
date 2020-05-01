import subprocess
import webbrowser
import glob
import os

def execute_test_doc(doc, comm):
    raw_command = r"{}".format(comm)
    subprocess.call([raw_command]+doc)

def open_doc_in_browser(path):
    website = get_latest_html_file(path)
    a_website = website
    webbrowser.open_new(a_website)

def get_latest_html_file(path):
    list_of_files = glob.glob(path+'\\*.html') # * means all if need specific format then *.html
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

