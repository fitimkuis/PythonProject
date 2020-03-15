*** Settings ***
Library           SeleniumLibrary

Suite TearDown    Close All Browsers

*** Test cases ***
Check the speed of your broadband
    Open Browser    http://www.fast.com    chrome    headlesschrome
    #Sleep    5
    #click element    id=speed-progress-indicator-icon
    Sleep    2
    #${speed}=    Get Text    id=speed-value
    Close Browser