*** Settings ***
Library    DataDriver    C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\my_data_file.csv    dialect=excel    delimiter=,   sheet_name=0    encoding=UTF-8
Library    SeleniumLibrary

Suite Setup         Open my Browser
Suite Teardown      Close Browsers
Test Setup          Open Login Page
Test Template       Invalid login

*** Variables ***

*** Test Cases ***       username        password
Login to Application    username    password

*** Keywords ***
Invalid login
    [Arguments]    ${username}    ${password}
    Input username    ${username}
    Input pwd    ${password}
    Click login button
    Run Keyword If    '${username}' == 'John Doe' and '${password}' == 'ThisIsNotAPassword'    Login Successful
    ...    ELSE    Error page should be visible

Input username
    [Arguments]    ${username}
    Input Text    css=#txt-username    ${username}

Input pwd
    [Arguments]    ${password}
    Input Text    css=#txt-password    ${password}

Click login button
    Click Element    css=#btn-login

Open my Browser
    Open Browser    http://demoaut.katalon.com/    chrome

Close Browsers
    Close All Browsers

Open Login Page
    Click Element    css=#btn-make-appointment

Error page should be visible
    Page Should Contain    Login failed!

Login Successful
    Page Should Contain    Make Appointment