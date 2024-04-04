from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"

@given('I am on the inventory page')
def inventoryPage(context):
    context.driver = webdriver.Chrome()
    context.driver.get(URL)
    context.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    context.driver.find_element(By.ID, 'login-button').click()
    WebDriverWait(context.driver, 10).until(EC.url_to_be(URL + 'inventory.html'))


@when('user sorts products from low price to high price')
def priceSort(context):
    element = context.driver.find_element(By.CLASS_NAME, "product_sort_container")
    dropdown = Select(element)
    dropdown.select_by_visible_text("Price (low to high)")


@when('user adds lowest priced product')
def lowestPriceProduct(context):
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()


@when('user clicks on cart')
def clickCart(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


@when('user clicks on checkout')
def clickCheckout(context):
    context.driver.find_element(By.ID, "checkout").click()


@when('user enters first name John')
def userFirstName(context):
    context.driver.find_element(By.ID, 'first-name').send_keys('John')


@when('user enters last name Doe')
def userLastName(context):
    context.driver.find_element(By.ID, 'last-name').send_keys('Doe')


@when('user enters zip code 123')
def userZipcode(context):
    context.driver.find_element(By.ID, 'postal-code').send_keys('123')


@when(u'user clicks Continue button')
def clickContinue(context):
    context.driver.find_element(By.ID, 'continue').click()


@then('I verify in Checkout overview page if the total amount for the added item is $8.63')
def verifyAmount(context):
    total = context.driver.find_element(By.CLASS_NAME, "summary_total_label").text
    amount = total.split(" ")
    assert amount[1] == '$8.63'


@when('user clicks Finish button')
def clickFinish(context):
    context.driver.find_element(By.ID, "finish").click()


@then('Thank You header is shown in Checkout Complete page')
def verifyCheckout(context):
    thank_you_header = context.driver.find_element(By.CLASS_NAME, "complete-header").text
    assert thank_you_header == 'Thank you for your order!'
    context.driver.save_screenshot("C:/Users/ARIEF/PycharmProjects/behaveProject/screenshots/orderPlacedSuccessful.png")
