import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

@pytest.fixture(scope="module")
def browser():
    selenium_host = os.getenv('SELENIUM_HOST', 'localhost')
    selenium_port = os.getenv('SELENIUM_PORT', '4444')
    selenium_url = f'http://{selenium_host}:{selenium_port}/wd/hub'
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=options,
        desired_capabilities=DesiredCapabilities.CHROME,
    )
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

@pytest.mark.search
def test_search(browser):
    browser.get("https://example.com")
    search_input = browser.find_element_by_name("q")
    search_input.send_keys("example search")
    search_input.submit()
    assert "Search Results" in browser.title

@pytest.mark.navigation
def test_navigation(browser):
    browser.get("https://example.com")
    link = browser.find_element_by_link_text("Some Link")
    link.click()
    assert "Expected Page" in browser.title

@pytest.mark.form_submission
def test_form_submission(browser):
    browser.get("https://example.com/form")
    text_input = browser.find_element_by_id("text_input")
    dropdown = browser.find_element_by_id("dropdown")
    checkbox = browser.find_element_by_id("checkbox")
    text_input.send_keys("sample text")
    dropdown.select_by_visible_text("Option 1")
    checkbox.click()
    submit_button = browser.find_element_by_xpath("//button[@type='submit']")
    submit_button.click()
    assert "Form submitted successfully" in browser.page_source
