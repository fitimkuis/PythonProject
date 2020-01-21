*** Settings ***
Library           SeleniumLibrary

*** Test cases ***
Check the speed of your broadband
    Open Browser    http://www.fast.com    chrome
    Sleep    10
    click element    id=speed-progress-indicator-icon
    Sleep    10
    ${speed}=    Get Text    id=speed-value
    Close Browser