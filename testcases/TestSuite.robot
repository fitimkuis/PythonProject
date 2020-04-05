*** Settings ***
Documentation    Suite description
Library          SeleniumLibrary
Library          OperatingSystem
Library          String
Library          Collections
Variables        variables/dict_variables.py
Library          scripts/parser_log.py
Library          Timer
Resource         keywords/TestSuiteKeywords.robot
Library          scripts/list_values.py
Library          webcolors
#Test Setup        Benchmark Setup
#Test Teardown     Benchmark TearDown

#Library           GuiStatusKeywords
#Suite Setup       Start Status UI
#Suite Teardown    Stop Status UI
*** Variables ***
${BROWSER}    chrome

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

ListVariablesPythonFileKeyword
    listvariables

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

DownloadPdfFileWithoutViewIt
    ${desired caps}    downloadPdfNotView
    Open Browser    https://www.google.com    browser=${BROWSER}    desired_capabilities=${desired caps}
    Close Browser

