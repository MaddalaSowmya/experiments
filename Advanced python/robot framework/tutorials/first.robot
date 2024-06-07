*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}  chrome
${URL}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
Login test
        open browser    ${URL}  ${BROWSER}
        Sleep       4s
        loginToApplication
        close browser

*** Keywords ***
loginToApplication
        maximize browser window
        Sleep    4s
        input Text  xpath://input[@name='username']     Admin
        input Text  xpath://input[@name='password']     admin123
        Sleep   2s
        click Element   xpath://button[@type='submit']
        sleep    2s
