*** Settings ***

Library             SeleniumLibrary
Library             test1.py
Library             DateTime
Force Tags          MyTag

*** Variables ***

${robotVar} =            FooBarBaz

*** Test Cases**
Foo Test Case
    [tags]              FooTag
    [Documentation]     Created by John Doe
    My Foo Bar Keyword  ${robotVar}
    Log                 ${robotVar}
    ${ret}              My Foo Bar Keyword  ${robotVar}
    Log                 ${ret}
    OpenGoogle


*** Keywords ***
My Foo Bar Keyword
    [Documentation]    Does so and so
    [Arguments]        ${arg1}
    Log                ${arg1}
    [Return]           ${arg1}

OpenGoogle
    do_some_stuff
    OpenBrowser     http://www.google.com  chrome
    Goto            https:www.tappara.fi
    #Sleep           2
    CloseBrowser
    ${date}         Get Current Date
    Log             ${date}

