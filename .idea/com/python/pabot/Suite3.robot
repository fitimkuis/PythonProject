*** Settings ***
Library           SeleniumLibrary

*** Test cases ***
Verify static data on web page
    Open Browser    http://www.fast.com    ff
    Sleep    5
    click element    xpath=//div[3]/div/div/div
    page should contain    FAST
    Close Browser