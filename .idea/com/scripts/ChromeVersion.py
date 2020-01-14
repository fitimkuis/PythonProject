from getFileProperties import *

chrome_browser = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe' #-- ENTER YOUR Chrome.exe filepath

cb_dictionary = getFileProperties(chrome_browser) # returns whole string of version (ie. 76.0.111)

chrome_browser_version = cb_dictionary['FileVersion'][:2] # substring version to capabable version (ie. 77 / 76)

nextVersion = str(int(chrome_browser_version) +1) # grabs the next version of the chrome browser

lastVersion = str(int(chrome_browser_version) -1) # grabs the last version of the chrome browser