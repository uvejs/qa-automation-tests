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

    @pytest.mark.order(100)
    def test_HomePage(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL)

        pageTitle = page.locator("#h-america-s-custom-carports-garages-and-metal-buildings").text_content()
        if pageTitle !='America’s Custom Carports, Garages, and Metal Buildings':
            allure.attach(page.screenshot(), name="pageTitleScreen", attachment_type=allure.attachment_type.PNG)
            assert False

        image20Year = page.locator("#post-6642 > div > div:nth-child(1) > div > div.wp-block-column.order-2.order-md-0.is-layout-flow.wp-block-column-is-layout-flow > div.wp-block-columns.are-vertically-aligned-center.is-not-stacked-on-mobile.is-layout-flex.wp-container-core-columns-layout-1.wp-block-columns-is-layout-flex > div:nth-child(1) > figure > img").is_visible()
        if image20Year ==False:
            allure.attach(page.screenshot(), name="image20Year", attachment_type=allure.attachment_type.PNG)
            assert False

        elementCarport= page.locator("#post-6642 > div > div:nth-child(1) > div > div:nth-child(2) > div > div.zipcode-product-type > form > div:nth-child(1) > div > label:nth-child(1) > span > span.afo-building-type-selector__item__mask-label").is_visible()
        if elementCarport == False:
            allure.attach(page.screenshot(), name="elementCarport", attachment_type=allure.attachment_type.PNG)
            assert False

        imageCustomerAndCounting= page.locator("#post-6642 > div > div.wp-block-group.box.mb-5.has-light-blue-background-color.has-background.box.mb-5.is-layout-constrained.wp-block-group-is-layout-constrained > div > div:nth-child(2) > figure > img").is_visible()
        if imageCustomerAndCounting == False:
            allure.attach(page.screenshot(), name="imageCustomerAndCounting", attachment_type=allure.attachment_type.PNG)
            assert False


    @pytest.mark.order(1001)
    def test_Metal_Carports(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL + "carports/")
        pageTitleCarports = page.locator("#h-custom-metal-carports-for-sale-from-1-295").text_content()
        if pageTitleCarports != "Custom Metal Carports for Sale from $1,295+":
            allure.attach(page.screenshot(), name="pageTitleCarports", attachment_type=allure.attachment_type.PNG)
            assert False

        imageResponsive = page.locator("#post-6067 > div > div:nth-child(2) > div > div > form > div > div.col-md-6.col--gutter.afo-pricing-calculator__col-right > div.afo-pricing-calculator__image > div > img").is_visible()
        if imageResponsive ==False:
            allure.attach(page.screenshot(), name="imageResponsive", attachment_type=allure.attachment_type.PNG)
            assert False

        imageMap = page.locator("#post-6067 > div > div.wp-block-group.pb-0.px-gutter.pb-0.pb-0.pb-0.px-gutter.box.px-gutter.is-layout-constrained.wp-container-core-group-layout-17.wp-block-group-is-layout-constrained > figure > img").is_visible()
        if imageMap == False:
            allure.attach(page.screenshot(), name="imageMap", attachment_type=allure.attachment_type.PNG)
            assert False


    @pytest.mark.order(1003)
    def test_Price_Your_Carport(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL + "products/carports/")
        pageTitlePrice_Your_Carpor = page.locator("#page > section.position-relative.afo-hero-block.has-bg-image.has-dark-layer.lazyloaded > div.container > div > h1").text_content()
        if pageTitlePrice_Your_Carpor != " Shop Alan’s Factory Outlet for the Best Deal on Carports":
            allure.attach(page.screenshot(), name="pageTitleCarports", attachment_type=allure.attachment_type.PNG)
            assert False

        contianer = page.locator("#page > section.position-relative.afo-hero-block.has-bg-image.has-dark-layer.lazyloaded > div.container").is_visible()
        if contianer ==False:
            allure.attach(page.screenshot(), name="contianer", attachment_type=allure.attachment_type.PNG)
            assert False

        title2 = page.locator("#page > section.pb-0.box.pt-3.mt-4.mt-lg-5 > div > div > h2").text_content()
        if title2 != ' Start With a Popular Configuration':
            allure.attach(page.screenshot(), name="title2", attachment_type=allure.attachment_type.PNG)
            assert False

        title3 = page.locator("#page > div:nth-child(6) > h2").text_content()
        if title3 != "Alan's Factory Outlet: Where to Buy a Carport at a Great Price":
            allure.attach(page.screenshot(), name="title3", attachment_type=allure.attachment_type.PNG)
            assert False

        testimonial = page.locator("#page > div.afo-testimonial > div > p:nth-child(1)").is_visible()
        if testimonial == False:
            allure.attach(page.screenshot(), name="testimonial", attachment_type=allure.attachment_type.PNG)
            assert False

        title4 = page.locator("#page > div.afo-price-and-design-block.afo-price-and-design-block--two-col > div > h2").text_content()
        if title4 != " Build Your Own Metal Garage or Carport With Our 3D Builder":
            allure.attach(page.screenshot(), name="title4", attachment_type=allure.attachment_type.PNG)
            assert False

        imageResponsive = page.locator("#page > div.afo-price-and-design-block.afo-price-and-design-block--two-col > div > div > div:nth-child(1) > a > img").is_visible()
        if imageResponsive ==False:
            allure.attach(page.screenshot(), name="imageResponsive", attachment_type=allure.attachment_type.PNG)
            assert False


    @pytest.mark.order(1004)
    def test_Carport_Cost(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL + "metal-carport-prices/")
        pageTitleCarport_Cost = page.locator("#post-6251 > div > div.wp-block-group.pt-lg-5.pb-5.pt-lg-5.pb-5.box.px-gutter.has-narrow-container.is-layout-constrained.wp-block-group-is-layout-constrained > h1").text_content()
        if pageTitleCarport_Cost != "Metal Carport Prices and Sizes [from $1,295 Installed]":
            allure.attach(page.screenshot(), name="pageTitleCarport_Cost", attachment_type=allure.attachment_type.PNG)
            assert False

        buttonCostumize = page.locator("#post-6251 > div > div.wp-block-group.pt-lg-5.pb-5.pt-lg-5.pb-5.box.px-gutter.has-narrow-container.is-layout-constrained.wp-block-group-is-layout-constrained > div.wp-block-buttons.is-content-justification-left.is-layout-flex.wp-container-core-buttons-layout-2.wp-block-buttons-is-layout-flex > div > a").is_visible()
        if buttonCostumize ==False:
            allure.attach(page.screenshot(), name="buttonCostumize", attachment_type=allure.attachment_type.PNG)
            assert False

        title2 = page.locator("#h-how-much-does-a-carport-cost > strong").text_content()
        if title2 != 'How Much Does a Carport Cost?':
            allure.attach(page.screenshot(), name="title2", attachment_type=allure.attachment_type.PNG)
            assert False

        imageWhiteCar= page.locator("#post-6251 > div > div.wp-block-group.pt-lg-5.pb-5.pt-lg-5.pb-5.box.px-gutter.has-narrow-container.is-layout-constrained.wp-block-group-is-layout-constrained > figure > img").is_visible()
        if imageWhiteCar ==False:
            allure.attach(page.screenshot(), name="imageWhiteCar", attachment_type=allure.attachment_type.PNG)
            assert False

        table1 =page.locator("#post-6251 > div > div.wp-block-group.pt-lg-5.pb-5.pt-lg-5.pb-5.box.px-gutter.has-narrow-container.is-layout-constrained.wp-block-group-is-layout-constrained > div:nth-child(11) > div > table.afo-pricing-table__table.afo-pricing-table__table--active").is_visible()
        if table1 == False:
            allure.attach(page.screenshot(), name="table1", attachment_type=allure.attachment_type.PNG)
            assert False

        table2 = page.locator("#post-6251 > div > div.wp-block-group.pt-lg-5.pb-5.pt-lg-5.pb-5.box.px-gutter.has-narrow-container.is-layout-constrained.wp-block-group-is-layout-constrained > div:nth-child(17) > div > table.afo-pricing-table__table.afo-pricing-table__table--active").is_visible()
        if table2 == False:
            allure.attach(page.screenshot(), name="table2", attachment_type=allure.attachment_type.PNG)
            assert False

        table3 = page.locator("#hs_cos_wrapper_widget_1500408286571 > div > div > table").is_visible()
        if table3 == False:
            allure.attach(page.screenshot(), name="table3", attachment_type=allure.attachment_type.PNG)
            assert False

    @pytest.mark.order(1005)
    def test_Pricing_Guides(self, browser_and_page):
        browser, page = browser_and_page
        page.goto(self.baseURL + "pricing-guides/")

        pageTitlePricing_Guides = page.locator("#post-6395 > div > div > div > h2").text_content()
        if pageTitlePricing_Guides != " Price Your Carport or Metal Garage":
            allure.attach(page.screenshot(), name="pageTitlePricing_Guides", attachment_type=allure.attachment_type.PNG)
            assert False

        imageMain= page.locator("#post-6395 > div > div > div > a:nth-child(2) > img").is_visible()
        if imageMain ==False:
            allure.attach(page.screenshot(), name="imageMain", attachment_type=allure.attachment_type.PNG)
            assert False

        goToCostCalculaortButton = page.locator("#post-6395 > div > div > div > a.btn.btn-primary").is_visible()
        if goToCostCalculaortButton == False:
            allure.attach(page.screenshot(), name="goToCostCalculaortButton", attachment_type=allure.attachment_type.PNG)
            assert False

        title2 = page.locator("#h-carport-and-metal-garage-pdf-price-list > span").text_content()
        if title2 != "Carport and Metal Garage PDF Price List":
            allure.attach(page.screenshot(), name="title2", attachment_type=allure.attachment_type.PNG)
            assert False