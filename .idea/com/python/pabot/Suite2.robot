*** Settings ***
Library           SeleniumLibrary

*** Test cases ***
Check the speed of your broadband
    Open Browser    http://www.fast.com    ff
    Sleep    15
    click element    id=speed-progress-indicator-icon
    Sleep    15
    ${speed}=    Get Text    id=speed-value
    Close Browser