*** Settings ***
Library           SeleniumLibrary

*** Test cases ***
suite1_open_web_page_successfully
    Open Browser    http://www.fast.com    chrome
    Sleep    10
    Capture Page Screenshot
    Close Browser