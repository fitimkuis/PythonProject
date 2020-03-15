*** Settings ***
Documentation    Suite description
Library          SeleniumLibrary
Library          OperatingSystem
Library          String
Library          Collections
Variables        .idea/com/python/dict_variables.py
Library          .idea/com/scripts/parser_log.py
Library           Timer
#Test Setup        Benchmark Setup
#Test Teardown     Benchmark TearDown

#Library           GuiStatusKeywords
#Suite Setup       Start Status UI
#Suite Teardown    Stop Status UI

*** Test Cases ***
Start And Stop
  Status UI Log               GuiStatus Demo
  ${count}=                   Set Variable    50
  Status UI Progressbar       ${count}
  :FOR   ${tick}   IN RANGE    ${count}
      Status UI Log           Processing ${tick}/${count}
      Status UI Action        step
  END

Example No 1 Passes
  Sleep   1 second

Example No 2 Passes
  Sleep   2 second

Verify So Far
  [Setup]       No Operation
  [Teardown]    No Operation
  Verify all Timers

Example No 3 Will Fail
  [Teardown]    No Operation
  Sleep   3 second
  Stop Timer    ${TEST NAME}
  Run Keyword And Expect Error     STARTS: Difference     Verify Single Timer   3   0    ${TEST NAME}

Final Verify Failure
  [Setup]       No Operation
  [Teardown]    No Operation
  Run Keyword And Expect Error     STARTS: Difference      Verify All Timers

Final Verify Without Failing
  [Setup]       No Operation
  [Teardown]    No Operation
  Verify All Timers   False

Can Start Timer
    Start Timer

Can Stop Timer
    Stop Timer

Can Check The Results
    ${res}=    Verify Single Timer   5   0
    Should Be True    ${res}

Can Throw Error
    Start Timer  error
    Sleep   5 seconds
    Stop Timer    error
    Run Keyword And Expect Error    STARTS: Difference      Verify Single Timer   3   0    error

LogParser
    parseLogFile
DictionaryVariablesPythonFile
    dictVariables

SimpleFireFoxTest
    Firefox

Chrome
    Open Browser    http://robotframework.org/     headlesschrome
    Capture Page Screenshot
    [Teardown]    Close All Browsers

OpenChromeBrowser
    ${DESIRED_CAPABILITIES}    IgnoreSSLCertification
    Open Browser    https://www.google.com    headlesschrome    desired_capabilities=${DESIRED_CAPABILITIES}
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
    #:FOR     ${i}    IN    ${list}
     ${result}   get_values      ${list}      ${CURDIR}${/}tasks_log.txt
     Log     ${result}
     ${string}    Convert To String     ${result}
     @{words}     Split String    ${string}   ,
     Create File    ${CURDIR}${/}tasks_duration.txt
     :FOR   ${i}    IN    @{words}
        Log    ${i}
        Append To File      ${CURDIR}${/}tasks_duration.txt     ${i}${\n}
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
    #Set To Dictionary   ${args}     chromeOptions    ${chrome default caps}
    Set To Dictionary    ${args}    acceptSslCerts    ${True}
    ${DESIRED_CAPABILITIES}    Create Dictionary    chromeOptions=${args}
    [Return]    ${DESIRED_CAPABILITIES}