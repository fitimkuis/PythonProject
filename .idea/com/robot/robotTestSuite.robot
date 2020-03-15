*** Settings ***

#Suite Setup      update-drivers
Suite TearDown    Close All Browsers

Library           DateTime
Library           String
Library           .idea/com/scripts/date_time.py
Library           .idea/com/scripts/excelUtil.py
Library           Collections
Library           OperatingSystem
Library           excelUtil
Library           SeleniumLibrary
Library           .idea/com/scripts/ChromeDriverAutomation.py
Library           .idea/com/scripts/run_pabot.py
Library           .idea/com/scripts/screenshot.py
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
    :FOR    ${key}    ${value}    IN    @{items}
    \    Log     The current key is: ${key}
    \    Log     The value is: ${value}