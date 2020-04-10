*** Settings ***
Library           webcolors
Library           scripts\\Colour.py
#Suite Setup      update-drivers
Suite TearDown    Close All Browsers

Library           DateTime
Library           String
Library           scripts\\date_time.py
Library           scripts\\excelUtil.py
Library           Collections
Library           OperatingSystem
Library           excelUtil
Library           SeleniumLibrary    plugins=SeleniumTestability;True;30 Seconds;True
Library           scripts\\ChromeDriverAutomation.py
Library           scripts\\run_pabot.py
Library           scripts\\screenshot.py
Resource          keywords\\TestSuiteKeywords.robot
#Library           .idea\\com\\python\\MyListener.py
Library           scripts\\date_time.py
Library           requests
Library           JSONLibrary
Library           ImapLibrary

*** Variables ***
${excel_path}     C:\\Users\\fitim\\AppData\\Local\\Programs\\Python\\Python37\\test.xls
${update}         ${EMPTY}

*** Test Cases ***
Use LSP service
    Open Browser    https://www.google.com  headlesschrome
    Sleep   1
    Close Browser

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

getJsonDictionary
    test dictionary

    Comment    "test": [
    Comment    {"firstname":"alex", "lastname":"leda"},
    Comment    {"firstname":"john", "lastname":"parsons"},
    Comment    {"firstname":"rick", "lastname":"roll"}
    Comment   ]

Example
    ${json}=    catenate    SEPARATOR=\n    {"test": [{"firstname":"alex", "lastname":"leda"},{"firstname":"john", "lastname":"parsons"},{"firstname":"rick", "lastname":"roll"}]}
    ${data}=  evaluate    json.loads('''${json}''')    json
    ${length}=   Get Length  ${data["test"][0]["firstname"]}
    ${max}=  Set variable  ${length-1}
    ${count}=  Set Variable    ${0}
    FOR  ${item}  IN RANGE  ${count}   ${max}
        ${firstname}  Set variable  ${data["test"][${item}]["firstname"]}
        ${status}  Run keyword and return status    Should be equal as strings   ${firstname}   john
        Run Keyword if  ${status}   Log to console  HERE ISS JOHNNY!
    END

Example2
    ${find-what}=    Set Variable    john
    ${json}=    catenate    SEPARATOR=\n    {"test": [{"firstname":"alex", "lastname":"leda"},{"firstname":"john", "lastname":"parsons"},{"firstname":"rick", "lastname":"roll"}]}
    ${data}=  evaluate    json.loads('''${json}''')    json
    ${firstname}=    Get Value From Json    ${data}    $..firstname    #return list
    #${length}=   Get Length  ${firstname}
    #Log    ${firstname}[2]
    #${i}    Set Variable    ${0}
    #FOR    ${x}    IN RANGE   ${i}   ${length}
    #${name}    Set Global Variable    ${EMPTY}
    FOR    ${x}    IN    @{firstname}
        #Log    ${x}
        #Log    ${firstname}[${i}]
        #Run Keyword If    '${firstname}[${i}]' == 'john'    Log To Console    Jonh is here
        #${name}    Run Keyword If    '${x}' == 'john'    myKeyword    ${x}
        Exit For Loop If    '${x}' == '${find-what}'
        #${i}    Evaluate    ${i} + 1
    END
    #Log To Console    ${x}
    Run Keyword If    '${x}'!= '${find-what}'    error-handling    ${find-what}
    ...    ELSE    Log To Console    ${x}
    #TODO
    #${length}=   Get Length  ${data["test"][0]["firstname"]}
    #${max}=  Set variable  ${length-1}
    #${count}=  Set Variable    ${0}
    #FOR  ${item}  IN RANGE  ${count}   ${max}
    #    ${firstname}  Set variable  ${data["test"][${item}]["firstname"]}
    #    ${status}  Run keyword and return status    Should be equal as strings   ${firstname}   john
    #    Run Keyword if  ${status}   Log to console  HERE ISS JOHNNY!
    #END

imapGmail
    imap






