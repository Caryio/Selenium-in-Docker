import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.login
def test_login(browser):
    browser.get("https://example.com/login")

    username_input = browser.find_element_by_id("username")
    password_input = browser.find_element_by_id("password")
    username_input.send_keys("your_username")
    password_input.send_keys("your_password")

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    assert "Dashboard" in browser.title

@pytest.mark.register
def test_register(browser):
    browser.get("https://example.com/register")

    username_input = browser.find_element_by_id("username")
    email_input = browser.find_element_by_id("email")
    password_input = browser.find_element_by_id("password")
    confirm_password_input = browser.find_element_by_id("confirm_password")
    username_input.send_keys("new_user")
    email_input.send_keys("new_user@example.com")
    password_input.send_keys("new_password")
    confirm_password_input.send_keys("new_password")

    register_button = browser.find_element_by_xpath("//button[@type='submit']")
    register_button.click()

    assert "Welcome" in browser.page_source

@pytest.mark.change_password
def test_change_password(browser):
    browser.get("https://example.com/change_password")

    current_password_input = browser.find_element_by_id("current_password")
    new_password_input = browser.find_element_by_id("new_password")
    confirm_new_password_input = browser.find_element_by_id("confirm_new_password")
    current_password_input.send_keys("current_password")
    new_password_input.send_keys("new_password")
    confirm_new_password_input.send_keys("new_password")

    change_password_button = browser.find_element_by_xpath("//button[@type='submit']")
    change_password_button.click()

    assert "Password changed successfully" in browser.page_source
