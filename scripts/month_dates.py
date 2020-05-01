'''
hi, maybe you can find something here you will need   *** Settings ***
Library           Selenium2Library
Library           DateTime
Library           ../../../../../Python27/month_dates.py
Library           String

*** Variables ***
${November}       30
${y}              1

*** Test Cases ***
date picker
    select date

*** Keywords ***
select date
    Open Browser    http://2008.kelvinluck.com/assets/jquery/datePicker/v2/demo/datePicker.html    ff
    Comment    Set Selenium Speed    0.3
    Click Element    xpath=/html/body/div[@id='container']/form[@id='chooseDateForm']/fieldset/ol/li[1]/a[@class='dp-choose-date']
    Comment    Click Element    xpath=//*[@title = 'Next month'][count(. | //*[text() = '>']) = count(//*[text() = '>'])]    #next month
    Comment    Page Should Contain    31
    Wait Until Element Is Visible    xpath=//*[text() = '29']    20
    Mouse Over    xpath=//*[text() = '29']
    Input Text    date1    28/12/2017
    Wait Until Keyword Succeeds    20    1    Click Element    //*[text() = '28']
    ${val}    Get Value    date1
    Should Be Equal    28/12/2017    ${val}
    Comment    ${my_date_to_select}    Get Current Date    UTC    6 days    %d/%m/%Y
    Comment    Execute JavaScript    document.getElementById("date1").value='${my_date_to_select}'
    ${date}    Get Current Date
    ${date}    Convert Date    ${date}    result_format=%Y%m%d
    Log    current date is ${date}
    ${date}    Split String To Characters    ${date}
    Log    Splitted date ${date}
    ${date}    Catenate    SEPARATOR=    ${date[6]}    ${date[7]}
    ${dat}    Convert To Integer    ${date}
    Log    ${dat}
    ${dates}    month_dates
    Comment    ${dates}    Evaluate    ${dates}+${dat}
    ${y}    Evaluate    '${dat}'
    Comment    Click Element    xpath=/html/body/div[@id='container']/form[@id='chooseDateForm']/fieldset/ol/li[1]/a[@class='dp-choose-date']    #click datepicker
    Click Element    //a[contains(text(),'Choose date')]
    Input Text    date1    28/12/2017
    Wait Until Keyword Succeeds    20    1    Click Element    xpath=//*[text() = '28']
    ${val}    Get Value    date1
    Should Be Equal    28/12/2017    ${val}
    Sleep    2
    : FOR    ${x}    IN RANGE    ${dates}
    \    Click Element    //a[contains(text(),'Choose date')]    #click datepicker
    \    Comment    Click Element    xpath=//*[@title = 'Next month'][count(. | //*[text() = '>']) = count(//*[text() = '>'])]    #click next month
    \    Wait Until Keyword Succeeds    20    1    Click Element    xpath=//*[text() = '${y}']
    \    ${val}    Get Value    date1
    \    Comment    Run Keyword If    '${val}'== '${EMPTY}'    rest of days    ${y}
    \    Run Keyword If    ${y}>26    rest of days    ${y}
    \    Run Keyword If    ${y}==${dates}    Exit For Loop
    \    ${y}    Evaluate    ${y}+1
    [Teardown]    Close All Browsers

rest of days
    [Arguments]    ${y}
    ${date}    Set Variable    ${y}/12/2017
    Input Text    date1    ${date}   and here my custom python lib import calendar
'''
import datetime
import calendar

def month_dates():
    now = datetime.datetime.now()
    print (calendar.monthrange(now.year,now.month)[1])
    return calendar.monthrange(now.year,now.month)[1]
