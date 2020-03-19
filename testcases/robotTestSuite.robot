*** Settings ***
Library           webcolors
Library           scripts/Colour.py
#Suite Setup      update-drivers
Suite TearDown    Close All Browsers

Library           DateTime
Library           String
Library           scripts/date_time.py
Library           scripts/excelUtil.py
Library           Collections
Library           OperatingSystem
Library           excelUtil
Library           SeleniumLibrary    plugins=SeleniumTestability;True;30 Seconds;True
Library           scripts/ChromeDriverAutomation.py
Library           scripts/run_pabot.py
Library           scripts/screenshot.py
Resource          keywords/TestSuiteKeywords.robot
#Library           .idea/com/python/MyListener.py

*** Variables ***
${excel_path}     C:/Users/fitim/AppData/Local/Programs/Python/Python37/test.xls
${update}         ${EMPTY}

*** Test Cases ***
Iterate Dictionary
    loop

SimpleFirefoxGoogleTest
    Open Browser    https://www.google.com    FireFox
    Sleep   4
    Close Browser

[Documentation]
Get Full Page Screenshot
    Open Browser    https://dzone.com/articles/perform-actions-using-javascript-in-python-seleniu    chrome
    Capture Full Page Screenshot
    Close Browser

Get Full Page
    Open Browser    https://stackoverflow.com/    chrome    headlesschrome
    Capture Full Page
    Close Browser

Get Full Page2
    take_fullpage_sceenshot   https://dzone.com/articles/perform-actions-using-javascript-in-python-seleniu

run-pabot-test-suites
    pabot
    rebot

combine test results
    rebot

date-time
    add date to date

exel-lib
    Comment    use-excel
    excel-keyword

Browser-test
    open-google-firefox
    Close All Browsers

ElementBackColour
    getElementColour


