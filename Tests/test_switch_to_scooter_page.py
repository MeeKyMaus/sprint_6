from page_objects.switch_to_scooter_page import SwitchToScooterPage
from locators.order_page_locators import OrderPageLocators
from locators.switch_to_scooter_page_locators import SwitchToScooterPageLocators
from Constants.constants_url import Constants_Url

class TestSwitchToScooter:
    def test_switch_to_scooter(self, driver):
        page = SwitchToScooterPage(driver)
        page.click_on_element(OrderPageLocators.HEADER_ORDER_BUTTON)
        page.click_on_element(SwitchToScooterPageLocators.SCOOTER_LOGO)
        url = driver.current_url
        assert url == Constants_Url.URL