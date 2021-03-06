*** Settings ***
Library          SeleniumLibrary
Library          OperatingSystem
Library          String
Library          Collections
Library          RobotTesting/com/testing/parse-log/parser_log.py
Library          RobotTesting/com/testing/parse-log/log_parser.py

*** Test Cases ***
Parse-TCS-BANK-Log
    bank-log-parser

LogParser
    parseLogFile

*** Keywords ***

bank-log-parser
     ${result}      get_log_values   ${CURDIR}${/}fi-point.log.2020-02-24.txt

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
