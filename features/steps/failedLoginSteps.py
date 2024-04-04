from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('I fill the account information for account LockedOutUser into the Username field and the Password field')
def userNamePassword(context):
    context.driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')


@then('I verify the Error Message contains the text "Sorry, this user has been banned."')
def verifyErrorMessage(context):
    context.driver.save_screenshot("C:/Users/ARIEF/PycharmProjects/behaveProject/screenshots/failedLoginPage.png")
    error_message = context.driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text
    assert "Sorry, this user has been banned." in error_message
