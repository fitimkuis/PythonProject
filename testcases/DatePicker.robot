*** Settings ***
Library           SeleniumLibrary
Library           DateTime
Library           scripts\\month_dates.py
Library           String

*** Variables ***
${November}       30
${y}              1

*** Test Cases ***
date picker
    select date

date picker2
    select date2

*** Keywords ***
select date
    Open Browser    http://2008.kelvinluck.com/assets/jquery/datePicker/v2/demo/datePicker.html    headlesschrome
    Click Link    \#
    Click Element    xpath=(.//td[contains(., '27')])[last()]
    ${val}    Get Value    date1
    Log To Console    ${val}
    ${month}=    Get Current Date
    ${month}=    Convert Date    ${month}    result_format=%m
    Log To Console    ${month}
    Should Be Equal    27/${month}/2020    ${val}
    ${date}    Get Current Date
    ${date}    Convert Date    ${date}    result_format=%Y%m%d
    Log    current date is ${date}
    ${date}    Split String To Characters    ${date}
    Log To Console    Splitted date ${date}
    ${date}    Catenate    SEPARATOR=    ${date[6]}    ${date[7]}
    ${dat}    Convert To Integer    ${date}
    Log To Console   ${dat}
    ${dates}    month_dates
    Log To Console    ${dates}
    ${y}    Evaluate    '${dat}'
    FOR    ${x}    IN RANGE    ${dates}
        Click Element    //a[contains(text(),'Choose date')]    #click datepicker
        Comment    Click Element    xpath=//*[@title = 'Next month'][count(. | //*[text() = '>']) = count(//*[text() = '>'])]    #click next month
        Clear Element Text    date1
        Click Element    xpath=//*[text() = '${y}']
        ${val}    Get Value    date1
        Run Keyword If    '${val}'== '${EMPTY}'    Click Element    xpath=(.//td[contains(., '${y}')])[last()]
        Run Keyword If    ${y}==${dates}    Exit For Loop
        ${y}    Evaluate    ${y}+1
    END
    [Teardown]    Close All Browsers

rest of days
    [Arguments]    ${y}
    ${date}    Set Variable    ${y}/12/2017
    Input Text    date1    ${date}

select date2
    Open Browser    http://2008.kelvinluck.com/assets/jquery/datePicker/v2/demo/datePicker.html    chrome
    Comment    Set Selenium Speed    0.3
    Click Element    xpath=(//a[contains(text(),'Choose date')])[2]
    Comment    Click Element    xpath=//*[@title = 'Next month'][count(. | //*[text() = '>']) = count(//*[text() = '>'])]    #next month
    Comment    Page Should Contain    31
    Wait Until Element Is Visible    xpath=//*[text() = '28']    20
    Mouse Over    xpath=//*[text() = '28']
    Input Text    date2    28/03/2020
    Clear Element Text    date2
    Wait Until Keyword Succeeds    20    1    Click Element    xpath=(.//td[contains(., '27')])[last()]
    ${val}    Get Value    date2
    Comment    Element Text Should Be    date2    27/12/2017
    Run Keyword If    '${val}'=='${EMPTY}'    Input Text    date2    28/03/2020
    ${val}    Get Value    date2
    Should Be Equal    27/03/2020    ${val}
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
    Click Element    xpath=(//a[contains(text(),'Choose date')])[2]
    Input Text    date2    28/03/2020
    Wait Until Keyword Succeeds    20    1    Click Element    xpath=//*[text() = '28']
    ${val}    Get Value    date2
    Comment    Should Be Equal    27/03/2020    ${val}
    FOR    ${x}    IN RANGE    ${dates}
        Click Element    xpath=(//a[contains(text(),'Choose date')])[2]    #click datepicker
        Comment    Click Element    xpath=//*[@title = 'Next month'][count(. | //*[text() = '>']) = count(//*[text() = '>'])]    #click next month
        Clear Element Text    date2
        Wait Until Keyword Succeeds    20    1    Click Element    xpath=//*[text() = '${y}']
        ${val}    Get Value    date2
        Run Keyword If    '${val}'== '${EMPTY}'    rest of days2    ${y}
        Comment    Run Keyword If    ${y}>26    rest of days2    ${y}
        Run Keyword If    ${y}==${dates}    Exit For Loop
        ${y}    Evaluate    ${y}+1
    END
    [Teardown]    Close All Browsers

rest of days2
    [Arguments]    ${y}
    ${date}    Set Variable    ${y}/03/2020
    Input Text    date2    ${date}
