*** Settings ***
Documentation    Suite description
Library          SeleniumLibrary
Library          Collections
Variables        .idea/com/python/dict_variables.py

*** Test Cases ***
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