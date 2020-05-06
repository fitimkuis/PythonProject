*** Settings ***
Library    OperatingSystem
Variables    variables\\counter.py
*** Keywords ***
Increment Counter
    Create File    ${CURDIR}/counter.py    counter=${counter+1}