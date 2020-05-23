*** Settings ***

Suite TearDown    Close All Browsers

Library           webcolors
Library           scripts\\Colour.py
#Suite Setup       update-drivers
Library           SerialLibrary    loop://    encoding=ascii
Library           SSHLibrary
Library           DateTime
Library           String
Library           scripts\\date_time.py
Library           scripts\\excelUtil.py
Library           Collections
Library           OperatingSystem
Library           excelUtil
Library           SeleniumLibrary    plugins=SeleniumTestability;True;30 Seconds;True    screenshot_root_directory=C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\TestSuitesSceenshots
Library           scripts\\ChromeDriverAutomation.py
Library           scripts\\run_pabot.py
Library           scripts\\screenshot.py
Resource          keywords\\TestSuiteKeywords.robot
#Library           .idea\\com\\python\\MyListener.py
Library           scripts\\date_time.py
Library           requests
Library           JSONLibrary
Library           ImapLibrary
#Library           DebugLibrary
#Library           AppiumLibrary
Library           scripts\\whole_suite.py
Library           clipboard
Library           scripts\\execute_document.py
Library           scripts\\xls_to_dict.py
Library           xmltodict
Library           pabotRunnerTest\\pabotRunner.py
Library           scripts\\ResultModifier.py

*** Variables ***
${excel_path}     C:\\Users\\fitim\\AppData\\Local\\Programs\\Python\\Python37\\test.xls
${update}         ${EMPTY}
${var}=    Set Variable    3

${QA03UatUrl}  https://uat01.mycompany.com:4567/
${v1}          QA03
${v2}          UatUrl

${f-name l-name}    Pat Mat
${fname}    f-name
${lname}    l-name

${URL}            https://test.com/

${docsource}=    robotTestSuite.robot
${dochtmlname}=    DemoTestHtmlDocument.html

${aaa}=   {aaa}

${xmlsource}=    C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\scripts\\demo.xml

${variable}=    ${{{'ADMIN': {'name': 'admin', 'pass': '123pass'}, 'USER': {'name': 'bobby', 'pass': 'aowiejf'}}}}

${pabot_path}=   C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\robotTestSuite.robot
${bat_path}=     C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\pabotRunnerTest\\pabotRunner.bat
${pabot_reports_file}=     C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\pabotRunnerTest\\reports
${run_path}=     C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\pabotRunnerTest

*** Test Cases ***
Execute PabotRunner
    #download_geckodriver
    #download_chromedriver
    ${filelist}=    Create List    ${pabot_path}    ${pabot_reports_file}    .robot
    execute_pabot_runner    ${bat_path}    ${filelist}

Inline Python
    [Tags]    smoke
    ${what}=    Set Variable   ['hello;', 'world;']
    Log To Console    ${{" ".join(${what})}}
    ${epoc}=    Get Current Date    result_format=epoch
    ${epoc}=    Convert To String    ${epoc}
    #@{matches}=    Get Regexp Matches    hello world    (hello) (world)    1    2
    #@{matches}=    Get Regexp Matches    hello world    h(....) w(....)    1    2
    @{matches}=    Get Regexp Matches    ${epoc}    (..........).(...)    1    2
    #${first}=    Set Variable    ${EMPTY}
    #${second}=    Set Variable    ${EMPTY}
    ${line}=    Set Variable    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    Log To Console    @{matches}
     FOR    ${match}    IN    @{matches}
         ${first}    ${second}=    Set Variable    ${match}
         Log To Console    ${first}    ${second}
     END
     ${result}=    Catenate    SEPARATOR=    ${first}    ${second}
     Log To Console    ${result}
     Log to Console    ${line}
     Log To Console    ${{datetime.datetime.fromtimestamp(${first}).strftime('%Y-%m-%d %H:%M:%S') }}
     Log To Console    ${{ time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(${first})) }}
    #1589954561.522866
    #with exclude millis it would be:
    #1589954561.0
    #but I need them, and without that float point:
    #1589954561522
    ##${epoch}=    Get Current Date    result_format=epoch
    ##${epoch}=    Convert To String    ${epoch}
    ##Log To Console    ${epoch}
    ##${splitted}=   Split String    ${epoch}    .
    #Log To Console    ${splitted}[0]
    #Log To Console    ${splitted}[1]
    ##${splitted2}=     Evaluate    ${splitted}[1][:3]
    ##${final}=    Catenate    SEPARATOR=    ${splitted}[0]    ${splitted2}
    ##Log To Console    ${final}
    #@{matches} =    Get Regexp Matches    1589954561.522866    (${splitted}[0]).(${splitted}[1])    1    2
    #Log To Console    @{matches}
    #FOR    ${match}    IN    @{matches}
    #    ${first}    ${second}=    Set Variable    ${match}
    #    Log To Console    ${first}    ${second}
    #END
    #Log To Console    @{matches}

    Log To Console    ${{{x:2**x for x in range(1,6)}}}

    ${BuildSqlQuery}=    Set Variable    ["use db1;delete from t1;","use db2;delete from t2;","use db3;delete from t3;"]
    Log To Console    ${{" ".join(${BuildSqlQuery})}}
    ${dd}=    Get Current Date    result_format=epoch
    Log To Console    ${dd}
    #${d1}=    Get Current Date    result_format=epoch
    Log To Console    ${{str(${dd})[:14].replace('.','')}}
    ${d}=    Get Current Date    result_format=epoch    exclude_millis=yes
    Log To Console    ${{int(${d})}}
    ${date}=    Get Current Date    result_format=%Y
    Log To Console    ${{datetime.date(${date}, 1, 1).strftime('%m/%d/%Y')}}
    Log To Console    ${variable}[ADMIN][name]



Year Start
    Log To Console    ${{decimal.Decimal('0.11')}}
    #Log To Console    ${{datatime.date(2020, 4, 27)}}
    Log To Console    ${{datetime.date.today()}}
    ${date}=    Get Current Date    result_format=%Y
    ${date}=    Evaluate    datetime.date(${date}, 1, 1).strftime('%m/%d/%Y')
    Log To Console    ${date}

    ${year}=    Evaluate    datetime.date.today().year
    Log To Console    ${year}
    ${year_start}=    Evaluate    datetime.date(${year}, 1, 1)
    Log To Console    ${year_start}
    ${year_first_day}=    Evaluate    datetime.date(${year}, 1, 1).strftime('%d/%m/%Y')
    Log To Console    ${year_first_day} format as day month Year

Create Dictonary from Xml
    #${XML_1}    Parse Xml    scripts/demo.xml
    ${XML_1}    Evaluate    xmltodict.parse(${xmlsource})
    Log To Consle    ${XML_1}
    #Log To Console    Parsing   ${XML_submitResourceAction}
    #@{body}=    Get Elements    ${XML_1}    *.//SPResource
    #${elemList}=    Get Elements    ${body}    1
    #@{elemList}=    Convert to List    ${elemList}
    #&{xmlDict}=    Create Dictionary
    #FOR    ${item}    IN    @{elemList}
    #    Set to Dictionary    ${xmlDict}    ${item.tag}=${item.text}
    #    Log To Console       ${xmlDict}
    #END

JavaScript
    Open Browser    http://demoaut.katalon.com/    chrome
    Wait Until Keyword Succeeds    20    1    Click Element    css=#btn-make-appointment
    ${matched elements}=    Get Webelements     xpath=//div
    Log To Console    ${matched elements}
    FOR  ${element}  IN    @{matched elements}
       ${text}=    Get Text    ${element}      # will get the text of each matched node
       Log To Console    ${text}
    END
    ${ret}=    Get WebElements    btn-make-appointment
    Log To Console    ${ret}
    ${ret}=    Execute Javascript    return document.getElementsByClassName("btn btn-dark btn-lg")
    Log To Console    ${ret}
    #Wait Until Keyword Succeeds    20    1    Execute Javascript    document.getElementById("btn-make-appointment.btn btn-dark btn-lg")[0].click()
    Wait Until Keyword Succeeds    20    1    Execute Javascript    document.getElementById("txt-username").value = 'John Doe'
    Wait Until Keyword Succeeds    20    1    Execute Javascript    document.getElementById("txt-password").value = 'ThisIsNotAPassword'
    Wait Until Keyword Succeeds    20    1    Click Element    css=#btn-login
    Close Browser

ExcelToDictionary
    Log To Console   ${aaa * 100}
    Log To Console   ${100 * 'aaa'}
    Log To Console   ${100 * '${aaa}'}
    ${dict1}=    get_all_data_from_excel_to_dic    C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/scripts/test.xls    sheet1
    ${len}=    Evaluate    len(${dict1})
    Log To Console    ${len}
    Log To Console    ${dict1}
    #${items}     Get Dictionary Items   ${dict1}[0]
    #Log To Console    ${items}
    FOR    ${i}    IN RANGE    ${len}
        ${items}=     Get Dictionary Items   ${dict1}[${i}]
        Log To Console    ${items}
        Iterate Excel Rows    ${items}
    END
    #FOR    ${val}    IN    @{items}
    #FOR    ${key}     ${value}    IN ZIP    ${dict1.keys()}    ${dict1.values()}
    #    Log To Console     ${val}
    #END

Run Test Document
    Log To Console     ${EXECDIR}
    Log To Console     ${CURDIR}
    ${doc}=    Create List    ${docsource}    ${dochtmlname}   ${CURDIR}
    execute_test_doc    ${doc}    ${EXECDIR}\\scripts\\run_test_doc.bat
    open_doc_in_browser    ${CURDIR}

ClipBorad Copy Paste
    clipboard

Run Suite Multiple Times
    ${file}=    Create List    ${EXECDIR}\\datadriven\\DataDrivenTest.robot
    execute_entire_suite    ${EXECDIR}\\scripts\\entire_suite.bat    ${file}

Run Entire Suite
    Log To Console    Run Entire Suite

Test Inline Expression
    ${new_URL}=    Set Variable    ${URL.replace('https:', 'http:')}
    Log To Console    ${new_URL}

Test One
    Open Browser    http://www.google.com    chrome
    Close Browser

Demo
    Log To Console    ${{datetime.date.today()}}
    Log To Console    ${{ {'id': 1, 'name': 'Example', 'children': [7, 9]} }}
    Log To Console    ${{len('${var}') > 3}}

Dynamic Variable
    Log To Console    ${${v1}${v2}}
    Log To Console    ${${fname}${lname}}


Use LSP service
    #download_chromedriver
    Open Browser    https://www.google.com  headlesschrome
    #Debug
    Sleep   1
    Close Browser

Iterate Dictionary
    loop

SimpleFirefoxGoogleTest
    Open Browser    https://www.google.com    FireFox
    Sleep   4
    Close Browser

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
    #[Setup]    Add Port    loop://    timeout=0.1
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
    Set Log Level	TRACE
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

Test
    pos and named    pos1    pos2    named=named1
*** Keywords ***
pos and named
    [Arguments]    ${pos}    ${pos2}    ${named}=name
    Log To Console    ${pos}
    Log To Console    ${named}

Iterate Excel Rows
    [Arguments]    ${items}
    FOR    ${val}    IN    @{items}
        Log To Console     ${val}
    END






