import pytest
import allure
from playwright.sync_api import sync_playwright
from random import randint


@allure.severity(allure.severity_level.NORMAL)
class TestUser:
    @pytest.fixture(scope="function")
    def browser(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome")
            yield browser
            browser.close()

    @pytest.mark.order(10003)
    def test_Register(self, browser):
        page = browser.new_page()
        page.goto("https://alansfactoryoutlet.com/my-account/")


        #random email
        random =randint(100000, 999999)
        email = "kastriot+" + str(random) + "@alansfactoryoutlet.com"

        # Fill in the username and password fields
        page.fill("input[name=email]",email)

        # Click the login button
        page.click("button[name=register]")

        # Check for error message
        try:
            # Wait for an element that contains the desired text
            page.wait_for_selector(
                'text="Your account was created successfully and a password has been sent to your email address."')

            # If the element is found, it means the message is displayed
            assert True
        except Exception as e:
            # If the element is not found within a timeout, it means the message is not displayed
            print("Message is not displayed.")
            assert False


    @pytest.mark.order(10004)
    def test_Login(self, browser):
        page = browser.new_page()
        page.goto("https://alansfactoryoutlet.com/my-account/")


        # Fill in the username and password fields
        page.fill("input[id=username]", "kastriot654020")
        page.fill("input[id=password]", "iwPcO6Xxz9zo")

        # Click the login button
        page.click("button[name=login]")

        # Check for error message
        error_element = page.locator("text=Error")
        if error_element.is_visible():
            allure.attach(page.screenshot(), name="testTitleScreen", attachment_type=allure.attachment_type.PNG)
            assert False
        else:
            assert True

