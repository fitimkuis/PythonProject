*** Settings ***
Library           webcolors
Library           scripts\\Colour.py
#Suite Setup      update-drivers
Suite TearDown    Close All Browsers

Library           SerialLibrary    #loop://    encoding=ascii
Library           SSHLibrary
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
    Comment    this is comment
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

Hello serial test
     Write Data    Hello World
     Read Data Should Be    Hello World

Read Until should read until terminator or size
    [Setup]    Add Port    loop://    timeout=0.1
    ${bytes} =    Set Variable
    Write Data    01 23 45 0A 67 89 AB CD EF
    ${read} =    SerialLibrary.Read Until
    Should Be Equal As Strings    ${read}    01 23 45 0A
    ${read} =    SerialLibrary.Read Until    size=2
    Should Be Equal As Strings    ${read}    67 89
    #${read} =    SerialLibrary.Read Until    terminator=CD
    #Should Be Equal As Strings    ${read}    AB CD
    ${read} =    SerialLibrary.Read Until    size=2
    Should Be Equal As Strings    ${read}    AB CD
    ${read} =    SerialLibrary.Read Until    size=1
    Should Be Equal As Strings    ${read}    EF
    ${read} =    SerialLibrary.Read Until
    Should Be Equal As Strings    ${read}    ${EMPTY}
    [Teardown]    Delete All Ports

Increment
    Create File    ${CURDIR}/increment.txt
    ${store}=    Create List
    ${ret}=    Create List
    Set Suite Variable    ${store}
    ${test}=    Set Variable    test
    ${index}=    Set Variable    ${100}
    FOR    ${i}    IN RANGE    10
        LOG    ${test}${index}
        Log To Console    ${test}${index}
        Append To List    ${store}    ${test}${index}    #values in a suite variable
        Append To File    ${CURDIR}/increment.txt    ${test}${index}\n    encoding=UTF-8    #values in a file
        ${index}    Evaluate    ${index} + 1
    END
    Log To Console     ${store}
    #read file
    ${content}=    OperatingSystem.Get File    ${CURDIR}/increment.txt    encoding=UTF-8
    Log To Console    ${content}
    @{lines}=    Split to lines    ${content}
    FOR    ${line}    IN    @{lines}
        ${Value}=    Get Variable Value    ${line}    #val from list to variable
        Append To List    ${ret}    ${line}
    END
    ${random value}=    Evaluate   random.choice($ret)    modules=random    #read ramdom value from the list (file)
    Log To Console    ${random value}

Increment In Every Test Run
    Log To Console    testcomp${counter}  # here you could also do Input Text or whatever
    Increment Counter

Example3
    ${NUMBER}=    Set Variable    ${100}
    Log To Console   Today is ${{datetime.date.today()}}.
    Log To Console    The lucky number is ${{random.randint(0, 100)}}.
    Log To Console    Number is ${NUMBER} and the next number is ${{$NUMBER + 1}}.
    #Log To Console    Lists and dicts are often needed with REST APIs:  ${{ {'id': 1, 'name': 'Example3', 'children': [7, 9]} }}
    Log To Console    Let's go crazy: ${{ {str(i): i for i in range($NUMBER)} }}.

GetLatLong
    Open Browser    C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\geo\\where.html   chrome
    Maximize Browser Window
    Click Element    css=#map_canvas > div:nth-child(2) > table > tr > td:nth-child(2) > button
    Sleep    1
    ${x}    Set Variable    ${0}
    ${args}=    Create Dictionary
    #${list}=    Create List
    FOR    ${i}    IN RANGE    6
        ${ret}=    Get Element Attribute    css=#gmimap${x} > area    title
        Log To Console    ${ret}
        ${ret}=    Fetch From Left    ${ret}    University
        ${ret}=    Replace String Using Regexp    ${ret}    (^[ ]+|[ ]+$)    \
        #Append To List    ${list}    ${ret}
        Set To Dictionary   ${args}    ${x}    ${ret}
        ${x}    Evaluate    ${x}+1
    END
    Log To Console    ${args}
    ${items}     Get Dictionary Items   ${args}
    FOR    ${key}    ${value}    IN    @{items}
        #Log To Console    ${key}
        Log To Console    ${value}
    END
    #${text}=    Get Element Attribute    css=#gmimap1 > area    title
    #${text2}=    Get Element Attribute    css=#gmimap2 > area    title
    #${text3}=    Get Element Attribute    css=#gmimap3 > area    title
    #${text4}=    Get Element Attribute    css=#gmimap4 > area    title
    #Set To Dictionary   ${args}    1    ${text}
    #Set To Dictionary   ${args}    2    ${text2}
    #Set To Dictionary   ${args}    3    ${text3}
    #Set To Dictionary   ${args}    4    ${text4}
    #Log To Console    ${text}
    #Log To Console    ${text2}
    #Log To Console    ${text3}
    #Log To Console    ${text4}
    #${text}=    Fetch From Left    ${text}    University
    #${text2}=    Fetch From Left    ${text2}    University
    #${text3}=    Fetch From Left    ${text3}    University
    #${text4}=    Fetch From Left    ${text4}    University
    #${text}=    Replace String Using Regexp    ${text}    (^[ ]+|[ ]+$)    \
    #${text2}=    Replace String Using Regexp    ${text2}    (^[ ]+|[ ]+$)    \
    #${text3}=    Replace String Using Regexp    ${text3}    (^[ ]+|[ ]+$)    \
    #${text4}=    Replace String Using Regexp    ${text4}    (^[ ]+|[ ]+$)    \
    #Log To Console    ${text}
    #Log To Console    ${text2}
    #Log To Console    ${text3}
    #Log To Console    ${text4}





