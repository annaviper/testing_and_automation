from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, driver):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Selenium 4


def after_scenario(context, driver):
    context.driver.quit()
