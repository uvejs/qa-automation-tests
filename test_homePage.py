import time

import pytest
import allure
from playwright.sync_api import sync_playwright

@allure.severity(allure.severity_level.NORMAL)
class TestHomeScreen:
    baseURL = 'https://alansfactoryoutlet.com/'

    @pytest.fixture(scope="class")
    def browser_and_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome")
            page = browser.new_page()
            page.set_viewport_size({'width': 1920, 'height': 1080})
            yield browser, page
            browser.close()

    @pytest.mark.order(1)
    def test_LogoHomePage(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL)

        logo_selector = '#page > header > div.header > div > div.main-header.afo-v-center.flex-wrap > div.logo > a > img'
        logo = page.query_selector(logo_selector)

        with allure.step("Check if logo exists"):
            if logo is  None:
                allure.attach(page.screenshot(), name="LogoExist", attachment_type=allure.attachment_type.PNG)
                assert False ,"Logo does not exist"

        with allure.step("Check if logo is loaded"):
            is_logo_loaded = page.evaluate(
                    f"document.querySelector('{logo_selector}').complete && document.querySelector('{logo_selector}').naturalHeight != 0")
            if is_logo_loaded == False:
                allure.attach(page.screenshot(), name="LogoNotLoaded", attachment_type=allure.attachment_type.PNG)
                assert False, "Logo is not loaded"


    @pytest.mark.order(2)
    def test_ContactInfoHeader(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL)

        InfoHeader = '#page > header > div.header > div > div.main-header.afo-v-center.flex-wrap > div.afo-v-center.site-utilities > div.customer-service.d-none.d-lg-flex.align-items-center.justify-content-center > div.header__nav-item.contact-info.afo-v-center > a'
        InfoHeaderElement = page.query_selector(InfoHeader)


        with allure.step("Check if Contact Info Header  exists"):
            if InfoHeaderElement is  None:
                allure.attach(page.screenshot(), name="InfoHeaderElement", attachment_type=allure.attachment_type.PNG)
                assert False ,"Contact Info Header does not exist"

        with allure.step("Check if Contact Info Header phone number is correct"):
            InfoHeaderElementText ="#page > header > div.header > div > div.main-header.afo-v-center.flex-wrap > div.afo-v-center.site-utilities > div.customer-service.d-none.d-lg-flex.align-items-center.justify-content-center > div.header__nav-item.contact-info.afo-v-center > a > span.contact-info__phone.d-none.d-lg-block"
            InfoHeaderElementText = page.query_selector(InfoHeader).text_content()

            time.sleep(1)
            if "Order Online or  1-888" not in InfoHeaderElementText:
                allure.attach(page.screenshot(), name="PhoneNumber", attachment_type=allure.attachment_type.PNG)
                assert False, "Phone Number is not Correct"

    @pytest.mark.order(3)
    def test_SearchButton(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL)

        SearchButton = "#page > header > div.header > div > div.main-header.afo-v-center.flex-wrap > div.afo-v-center.site-utilities > div.header__nav-item.order-lg-1.me-3.me-lg-0 > button"
        SearchButtonElement = page.query_selector(SearchButton)


        with allure.step("Check if Search Button exists"):
            if SearchButtonElement is  None:
                allure.attach(page.screenshot(), name="SearchButtonElement", attachment_type=allure.attachment_type.PNG)
                assert False ,"Search Button does not exist"

    @pytest.mark.order(4)
    def test_DeliverToElement(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL)

        DeliverTO = "#page > header > div.header > div > div.main-header.afo-v-center.flex-wrap > div.afo-v-center.site-utilities > div.header__nav-item.order-lg-2.d-none.d-lg-block > div > div > button > p.zipcode__label.text-start.me-2.me-lg-0"
        DeliverTOElement = page.query_selector(DeliverTO)

        with allure.step("Check if Deliver To exists"):
            if DeliverTOElement is None:
                allure.attach(page.screenshot(), name="DeliverTOElement", attachment_type=allure.attachment_type.PNG)
                assert False, "Deliver To element does not exist"


    @pytest.mark.order(5)
    def test_AccountElement(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL)

        Account = "#page > header > div.header > div > div.main-header.afo-v-center.flex-wrap > div.afo-v-center.site-utilities > nav > div.header__nav-item.order-1.d-none.d-lg-block > a > span.utility__label.d-none.d-xl-inline-flex"
        AccountElement = page.query_selector(Account)

        with allure.step("Check if Account Element exists"):
            if AccountElement is None:
                allure.attach(page.screenshot(), name="AccountElement", attachment_type=allure.attachment_type.PNG)
                assert False, "Account element does not exist"

    @pytest.mark.order(6)
    def test_CardElement(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL)

        Card = "#page > header > div.header > div > div.main-header.afo-v-center.flex-wrap > div.afo-v-center.site-utilities > nav > div.header__nav-item.order-3 > a > span.utility__label.d-none.d-xl-inline-flex"
        CardElement = page.query_selector(Card)

        with allure.step("Check if Card Element exists"):
            if CardElement is None:
                allure.attach(page.screenshot(), name="CardElement", attachment_type=allure.attachment_type.PNG)
                assert False, "Card element does not exist."