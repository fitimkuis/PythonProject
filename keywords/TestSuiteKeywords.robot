*** Settings ***
#Library           webcolors
#Library           scripts/convert_rgb.py
Variables   variables/counter.py
*** Variables ***
${OS}    Win10
${JOBS}    RobotTest
*** Keywords ***
pabot
    run_pabot.Execute Pabot

rebot
    run_pabot.Execute Rebot

download-chromedriver
    download_chromedriver

update-drivers
    download_geckodriver
    download_chromedriver
    ${update}       autoupdate_chromedriver
    Log        ${update}
open-google-firefox
    Open Browser    https://www.google.com      ff
    Sleep   5
    Close Browser


add date to date
    ${date}    Get Current Date
    ${date}    Convert Date    ${date}    result_format=%y%m%d
    Log    current date is ${date}
    ${date}    Get Current Date
    ${date}    Convert Date    ${date}    result_format=%Y%m%d
    Log    current date is ${date}
    ${date}    Split String To Characters    ${date}
    Log    Splitted date ${date}
    ${date}    Catenate    SEPARATOR=    ${date[2]}    ${date[3]}    ${date[4]}    ${date[5]}    ${date[6]}    ${date[7]}
    Log    Catenated date ${date}
    ${date}    Get Current Date
    ${date}    Subtract Time From Date    ${date}    7 days
    ${date}    Convert Date    ${date}    result_format=%d/%m/%Y
    Comment    ${date}    Convert Date    ${date}    result_format=%Y-%m-%d %H:%M:%S.%f
    ${curr_date}    Get Current Date
    ${addDays}    Set Variable    -3
    ${output_format}    Set Variable    %Y-%m-%d %H:%M:%S.%f
    ${another_date}    get_date    ${curr_date}    ${output_format}    ${addDays}
    ${another_date}    Convert Date    ${another_date}    result_format=%d/%m/%Y
    Comment    ${date2}    Subtract Time From Date    ${another_date}    7
    Comment    ${date2}    Subtract Date From Date    ${date}    ${another_date}
    Comment    ${date2}    Convert Date    ${date2}    result_format=%d/%m/%Y
    #exclude_milles=yes    date_format=%m.%d.%Y %H:%M    result_format=%d/%m/%Y    result_format=%Y-%m-%d %H:%M:%S.%f

use-excel
     Open Excel    C:/Users/fitim/AppData/Local/Programs/Python/Python37\test.xls
     Comment    Add New Sheet    sheet2
     ${data}    Read Cell Data By Coordinates    sheet1    1    0
     Comment    Put Date To Cell    sheet1    1    1    Heippa
     Comment    Put Number To Cell    sheet1    0    0    10
     Comment    Put Number To Cell    sheet1    0    0    10
     Put String To Cell    sheet2    1    0    Moi
     Comment    Put String To Cell    Taulukko1    0    1    AB
     Comment    Put String To Cell    Taulukko1    0    2    AC
     Comment    Put String To Cell    Taulukko1    0    3    AD
     Comment    Save Excel    C:/Users/fitim/Desktop/robot_test_cases/test.xls

excel-keyword
    Comment    writeExcel    ${CURDIR}/test.xls
    Comment    make_my_class    ${excel_path}
    init_excel    C:/Users/fitim/AppData/Local/Programs/Python/Python37/test.xls
    write_excel_file
    Log    read_excel_file
    Comment    ${cell}    read_excel_file
    Comment    Log    ${cell}
    Comment    Should be equal    ${cell}    A1

loop
    ${mydict}    Create Dictionary      a=1    b=2      c=3     d=4
    ${items}     Get Dictionary Items   ${mydict}
    FOR    ${key}    ${value}    IN    @{items}
         Log     The current key is: ${key}
         Log     The value is: ${value}
    END

Benchmark Setup
  Configure Timer   3 seconds   0 seconds   ${TEST NAME}
  Start Timer   ${TEST NAME}

Benchmark TearDown
  Stop Timer    ${TEST NAME}
  Verify Single Timer    3 seconds   0 seconds   ${TEST NAME}

parseLogFile
     ${list}    Create List
     ${list}   get_unique_task_names       ${CURDIR}${/}tasks_log.txt
     Log    ${list}
    #FOR     ${i}    IN    ${list}
     ${result}   get_values      ${list}      ${CURDIR}${/}tasks_log.txt
     Log     ${result}
     ${string}    Convert To String     ${result}
     @{words}     Split String    ${string}   ,
     Create File    ${CURDIR}${/}tasks_duration.txt
     FOR   ${i}    IN    @{words}
        Log    ${i}
        Append To File      ${CURDIR}${/}tasks_duration.txt     ${i}${\n}
     END

dictVariables
    Log    ${MYORDRDICT}
    ${items}     Get Dictionary Items   ${MYORDRDICT}
    FOR    ${key}    ${value}    IN    @{items}    #iterate dynamic orderdict
         Log     The current key is: ${key}
         Log     The value is: ${value}
    END
    Log    ${FINNISH.cat}
    LogMany   ${SALARIES.Pat}    ${SALARIES.Mat}
    FOR    ${key}    IN    @{SALARIES.keys()}
        Log    ${SALARIES["${key}"]}
    END
    ${items}     Get Dictionary Items   ${SALARIES}    #iterate static defined orderdict
    FOR    ${key}    ${value}    IN    @{items}
         Log     The current key is: ${key}
         Log     The value is: ${value}
    END

listvariables
    [arguments]
    Log    ${JOBS}
    ${cnt}=    Get length    ${JOBS}    #get list lenght
    Log    ${cnt}
    ${y}    Convert To Integer    ${cnt}    #convert list lenght to integer
    FOR    ${index}    IN RANGE    ${y}     #static count given by code
        Log    ${JOBS}[${index}]
    END
    #Generate dynamic works list number given by user
    @{WORKS}    Generate Works    10
    Log    ${WORKS}
    ${cnt}=    Get length    ${WORKS}    #get list lenght
    Log    ${cnt}
    ${y}    Convert To Integer    ${cnt}    #convert list lenght to integer
    FOR    ${index}    IN RANGE    ${y}
        Log    ${WORKS}[${index}]
    END

Provided precondition
    Setup system under test

Firefox
    Open Browser    https://www.google.com    firefox
    Sleep    4
    Close Browser

IgnoreSSLCertification
    ${chrome default caps}    Evaluate    sys.modules['selenium.webdriver'].common.desired_capabilities.DesiredCapabilities.CHROME    sys, selenium.webdriver
    ${list}    Create List    --ignore-ssl-errors    --allow-insecure-localhost    --allow-running-insecure-content
    ${args}    Create Dictionary    args=${list}
    Set To Dictionary   ${args}     chromeOptions    ${chrome default caps}
    Set To Dictionary    ${args}    acceptSslCerts    ${True}
    ${DESIRED_CAPABILITIES}    Create Dictionary    chromeOptions=${args}
    [Return]    ${DESIRED_CAPABILITIES}

downloadPdfNotView
    ${list} =     Create List    --start-maximized    --disable-web-security
    ${args} =     Create Dictionary    args=${list}
    ${desired caps} =     Create Dictionary    chromeOptions=${args}
    [Return]    ${desired_caps}

getElementColour
    Open Browser    http://demoaut.katalon.com/    chrome
    ${x}=   Is Testability Installed
    Should Be True    ${x}
    ${bgcolor}    Execute Javascript    return document.defaultView.getComputedStyle(document.getElementById("btn-make-appointment"),null)['background-color']
    Log    ${bgcolor}
    ${col}=   Colour.fetch_colour_name    ${bgcolor}
    Log    ${col}
    ${hex}    Colour.convert_to_hex
    Click Element    btn-make-appointment
    #Wait For Testability Ready
    Input Text    txt-username    John Doe
    Input Text    txt-password     ThisIsNotAPassword
    Click Element    btn-login
    #Wait For Testability Ready
    ${bgcolor}    Execute Javascript    return document.defaultView.getComputedStyle(document.getElementById("combo_facility"),null)['background-color']
    ${col}=   Colour.fetch_colour_name    ${bgcolor}
    Log    ${col}
    ${hex}    Colour.convert_to_hex
    Close Browser

test dictionary
    ${result} =  get  http://api.zippopotam.us/us/ma/belmont
    Should Be Equal  ${result.status_code}  ${200}
    ${json} =  Set Variable  ${result.json()}
    ${longitude}=    Get Value From Json    ${json}    $..longitude    #return list
    Log    ${longitude[0]}
    ${latitude}=    Get Value From Json    ${json}    $..latitude    #return list
    Log    ${latitude[0]}
    ${zip}=    Set Variable    post code    #key has space
    ${postal code}=    Get Value From Json    ${json}    $..'${zip}'    #return list
    Log    ${postal code[0]}
    ${city}=    Get Value From Json    ${json}    $..'place name'    #return list
    Log    ${city[0]}
    FOR    ${key}    IN    @{json.keys()}
        Log    ${json["${key}"]}
    END
    ${country} =  Get From Dictionary  ${json}  country abbreviation
    Should Be Equal  ${country}  US
    ${places} =  Get From Dictionary  ${json}  places
    Log    ${places[0]}
    FOR    ${place}    IN    ${places}
        ${place name}=    Get From Dictionary   ${json}    place name
        ${state}=    Get From Dictionary   ${json}    state
        ${state abbreviation}=    Get From Dictionary    ${json}    state abbreviation
        ${long}=    Get Value From Json    ${json}    $..longitude
    END

imap
    Open Mailbox    host=smtp.gmail.com    user=fitimkuis@gmail.com    password=ModeeMi16
    ${LATEST}=    Wait for Mail    fromEmail=timo.kuisma@sci.fi    toEmail=fitimkuis@gmail.com    timeout=150
    Log    ${LATEST}
    #${HTML}=    Open Link from Mail    ${LATEST}
    #Comment    Should Contain    ${HTML}    Your email address has been updated
    Close Mailbox

myKeyword
    [arguments]    ${x}
    ${name}=    set Global variable    ${x}
    [Return]    ${name}

error-handling
    [arguments]    ${x}
    Fail    ${x} was not there

Increment Counter
    Create File    ${CURDIR}/variables/counter.py    counter=${counter+1}



