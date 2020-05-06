*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           scripts\\TakeScreenshot.py
Library           scripts\\ImRead.py
Library           scripts\\CompareImages.py


*** Test Cases ***
Get File
    Log To Console    testcases\2019-06-08 14 29 18_screenshot.png

compare images
    compare image

*** Keywords ***
compare image
    Wait Until Keyword Succeeds    40    1    Open Browser    https://www.google.com    Chrome
    Set selenium speed    0.3
    Maximize Browser Window
    #${width}    Execute JavaScript    return document.querySelector('#hplogo > a > img').offsetWidth;
    #${hight}    Execute JavaScript    return document.querySelector('#hplogo > a > img').offsetHeight;
    Capture Element Screenshot    css=#hplogo > a > img    testcases/images/google1.png
    #Log To Console    ${width} ${hight}
    #${x1}    Get Horizontal Position    css=#hplogo > a > img
    #${y1}    Get Vertical Position    css=#hplogo > a > img
    #Log To Console    ${x1} ${y1}
    #${x2}    evaluate    ${x1}+ 542
    #${y2}    evaluate    ${y1} + 200
    #${y1}    evaluate    ${y1} + 170
    #${imfile}    image screenshot    ${x1}    ${x2}    ${y1}    ${y2}
    #${image text}    Read Image Text    testcases/images/google.png
    ${ret}    CompareImages.Comp Images    testcases/images/google1.png    testcases/images/google2.png
    Log To Console    ${ret}
    CloseBrowser
    [Teardown]    CloseBrowser

