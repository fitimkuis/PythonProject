*** Settings ***
Documentation    Suite description
Library          SeleniumLibrary
Library          OperatingSystem
Library          String
Library          Collections
Variables        .idea/com/python/dict_variables.py
Library          .idea/com/scripts/parser_log.py

*** Test Cases ***

LogParser
    parseLogFile
DictionaryVariablesPythonFile
    dictVariables

SimpleFireFoxTest
    Firefox

OpenChromeBrowser
    ${DESIRED_CAPABILITIES}    IgnoreSSLCertification
    Open Browser    https://www.google.com    chrome    desired_capabilities=${DESIRED_CAPABILITIES}
    Sleep    2
    Close Browser


Test title
    [Tags]    DEBUG
    Provided precondition
    When action
    Then check expectations

Foo Test Case
    [tags]              FooTag
    [Documentation]     Created by John Doe
    My Foo Bar Keyword  ${robotVar}
    Log                 ${robotVar}
    ${ret}              My Foo Bar Keyword  ${robotVar}
    Log                 ${ret}
    OpenGoogle

*** Keywords ***
parseLogFile
     ${list}    Create List
     ${list}   get_unique_task_names       ${CURDIR}${/}tasks_log.txt
     Log    ${list}
    #:FOR     ${i}    IN    ${list}
     ${result}   get_values      ${list}      ${CURDIR}${/}tasks_log.txt
     Log     ${result}
     ${string}    Convert To String     ${result}
     @{words}     Split String    ${string}   ,
     :FOR   ${i}    IN    @{words}
        Log    ${i}
     END


dictVariables
    Log   ${FINNISH.cat}
    LogMany   ${SALARIES.Pat}    ${SALARIES.Mat}
    :FOR    ${key}    IN    @{SALARIES.keys()}
    \   Log    ${SALARIES["${key}"]}
    ${items}     Get Dictionary Items   ${SALARIES}
    :FOR    ${key}    ${value}    IN    @{items}
    \    Log     The current key is: ${key}
    \    Log     The value is: ${value}


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
    Set To Dictionary    ${args}    acceptSslCerts    ${True}
    ${DESIRED_CAPABILITIES}    Create Dictionary    chromeOptions=${args}
    [Return]    ${DESIRED_CAPABILITIES}