from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"


@given('I am on the Demo Login Page')
def demoLoginPage(context):
    context.driver = webdriver.Chrome()
    context.driver.get(URL)


@when('I fill the account information for account StandardUser into the Username field and the Password field')
def userNamePassword(context):
    context.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')


@when('I click the Login Button')
def clickloginButton(context):
    context.driver.find_element(By.ID, 'login-button').click()


@then('I am redirected to the Demo Main Page')
def verifyDemoMainPage(context):
    WebDriverWait(context.driver, 10).until(EC.url_to_be(URL + 'inventory.html'))
    context.driver.save_screenshot("C:/Users/ARIEF/PycharmProjects/behaveProject/screenshots/successfulLoginPage.png")


@then('I verify the App Logo exists')
def verifyLogo(context):
    try:
        logo = context.driver.find_element(By.CLASS_NAME, 'MuiStack-root css-19diydd').is_displayed()
    except:
        context.driver.close()
        assert False, "Login successful and exact logo is not displayed"
    if logo == True:
        context.driver.close()
        assert True, "Logo is displayed"
