*** Settings ***
Library           SeleniumLibrary

Suite TearDown    Close All Browsers

*** Test cases ***
suite1_open_web_page_successfully
    Open Browser    http://www.fast.com    chrome    headlesschrome
    Sleep    10
    Capture Page Screenshot
    Close Browser