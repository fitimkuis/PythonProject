*** Settings ***
Library           Browser
#Library           RPA.Browser

*** Variables ***
${URL}=    https://robotsparebinindustries.com/

*** Keywords ***
Open The Intranet Website
    Open Available Browser    ${URL}

Log In
    Input Text    username    maria
    Input Password    password    thoushallnotpass
    Submit Form

*** Tasks ***
Open the intranet site and log in
    Open The Intranet Website
    Log In

Use asserts
    Open Browser
    New Page    https://robotsparebinindustries.com
    Get Title    ==    RobotSpareBin Industries Inc. - Intranet
    Get Title    validate    value == "RobotSpareBin Industries Inc. - Intranet"
    Get Attribute    meta    charset    ==    utf-8
    Get Url    ==    https://robotsparebinindustries.com/#/

Open a browser in GUI mode
    Open Browser
    New Page    https://playwright.dev
    #Get Text    h1    contains    Playwright