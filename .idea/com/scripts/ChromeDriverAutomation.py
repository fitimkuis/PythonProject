from ChromeVersion import chrome_browser_version, nextVersion, lastVersion
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from webdriverdownloader import GeckoDriverDownloader

def download_geckodriver():
    gdd = GeckoDriverDownloader()
    gdd.download_and_install()

def autoupdate_chromedriver():

    driverName = "/chromedriver.exe"

    # defining base file directory of chrome drivers
    driver_loc = "C:/Users/fitim/IdeaProjects/PythonProject/"
    #driver_loc = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\" #-- ENTER the file path of your exe
    # -- I created a separate folder to house the versions of chromedriver, previous versions will be deleted after downloading the newest version.
    # ie. version 75 will be deleted after 77 has been downloaded.

    # defining the file path of your exe file automatically updating based on your browsers current version of chrome.
    #currentPath = driver_loc + chrome_browser_version + driverName
    currentPath = driver_loc + driverName
    # check file directories to see if chrome drivers exist in nextVersion


    import os.path

    # check if new version of drive exists --> only continue if it doesn't
    Newpath = driver_loc + nextVersion
    match = False
    driver = webdriver.Chrome()
    str1 = driver.capabilities['browserVersion']
    str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
    print(str1)
    print(str2)
    print(str1[0:2])
    print(str2[0:2])
    if str1[0:2] != str2[0:2]:
        print("please download correct chromedriver version")
        match = True
    else:
        print("chrome and driver match")

    driver.quit()

    # check if we have already downloaded the newest version of the browser, ie if we have version 76, and have already downloaded a version of 77, we don't need to run any more of the script.
    newfileloc = Newpath + driverName
    exists = os.path.exists(newfileloc)


    if (exists == False and match == True):

        #open chrome driver and attempt to download new chrome driver exe file.
        chrome_options = Options()
        executable_path = currentPath
        driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)

        # opening up url of chromedriver to get new version of chromedriver.
        chromeDriverURL = 'https://chromedriver.storage.googleapis.com/index.html?path=' + nextVersion

        driver.get(chromeDriverURL)

        time.sleep(5)
        # find records of table rows
        table = driver.find_elements_by_css_selector('tr')


        # check the length of the table
        Table_len = len(table)

        # ensure that table length is greater than 4, else fail. -- table length of 4 is default when there are no availble updates
        if (Table_len > 4 ):

            # define string value of link
            rowText = table[(len(table)-2)].text[:6]
            time.sleep(1)
            # select the value of the row
            driver.find_element_by_xpath('//*[contains(text(),' + '"' + str(rowText) + '"'+')]').click()
            time.sleep(1)
            #select chromedriver zip for windows
            driver.find_element_by_xpath('//*[contains(text(),' + '"' + "win32" + '"'+')]').click()

            time.sleep(3)
            driver.quit()

            from zipfile import ZipFile
            import shutil


            fileName = r"C:\Users\fitim\Downloads\chromedriver_win32.zip" #--> enter your download path here.


            # Create a ZipFile Object and load sample.zip in it
            with ZipFile(fileName, 'r') as zipObj:
                # Extract all the contents of zip file in different directory
                zipObj.extractall(Newpath)


            # delete downloaded file
            os.remove(fileName)

            # defining old chrome driver location
            oldPath = driver_loc + lastVersion
            oldpathexists = os.path.exists(oldPath)

            # this deletes the old folder with the older version of chromedriver in it (version 75, once 77 has been downloaded)
            if(oldpathexists == True):
                shutil.rmtree(oldPath, ignore_errors=True)

    if match == False:
        return "no needed to do update"
    else:
        return "Done chromedriver update to version ",nextVersion

    #exit()