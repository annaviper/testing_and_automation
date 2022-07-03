from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('I navigate to the Google website')
def step_impl(context):
    # ACCEPT ALL COOKIES
    context.driver.get("https://google.com")
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()


@when('I enter "{text}" in the search bar and click search')
def step_impl(context, text):
    title = context.driver.title
    print(f"\tTitle is: {title}")
    assert "Google" in title

    context.driver.find_element_by_name("q").send_keys(text, Keys.RETURN)


@then('I can see results related to "{text}"')
def step_impl(context, text):
    context.driver.find_element(By.ID, "rso")
