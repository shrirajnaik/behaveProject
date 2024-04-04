from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
URL = "https://www.saucedemo.com/"

driver.get(URL)
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()
WebDriverWait(driver, 10).until(EC.url_to_be(URL + 'inventory.html'))

element = driver.find_element(By.CLASS_NAME, "product_sort_container")
dropdown = Select(element)
dropdown.select_by_visible_text("Price (low to high)")

driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, 'first-name').send_keys('John')

driver.find_element(By.ID, 'last-name').send_keys('Doe')

driver.find_element(By.ID, 'postal-code').send_keys('123')

driver.find_element(By.ID, 'continue').click()

total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
print(total)
amount = total.split(" ")
print(amount[1])
assert amount[1] == '$8.63'

driver.find_element(By.ID, "finish").click()

thank_you_header = driver.find_element(By.CLASS_NAME, "complete-header").text
print(thank_you_header)
assert thank_you_header == 'Thank you for your order!'

