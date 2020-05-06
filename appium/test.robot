*** Settings ***
Library     AppiumLibrary
Library     ${EXECDIR}${/}appium_helper.py
Suite Setup    Start Appium Server
Suite Teardown     Stop Appium Server


Appium
    Log To Console    play with appium
