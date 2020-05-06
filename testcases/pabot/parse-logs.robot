*** Settings ***
Library          SeleniumLibrary
Library          OperatingSystem
Library          String
Library          Collections
Library          scripts/parser_log.py
#Library          scripts/new_log_parser.py
Resource         keywords/ParseLogKeywords.robot

*** Test Cases ***
Parse-TCS-BANK-Log
    bank-log-parser

LogParser
    parseLogFile

