import pytest

from pages.checkout_page import checkout_page
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utilities.utils import utils


@pytest.mark.usefixtures("setup")
class TestSerchandOrderMobile:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.sp = ShopPage(self.driver)
        self.co = checkout_page(self.driver)
        self.ut = utils(self.driver)
    def test_ordermobile(self):
        #launching the browser and opening the website
        #proving username and password and click on login
        # lp=LoginPage(self.driver)
        self.lp.login("rahulshettyacademy","Learning@830$3mK2")
        # Wait for products to load
        # Find products and add "Blackberry" to cart
        # sp=ShopPage(self.driver)
        self.sp.scroll()
        self.sp.mobile_selection("Blackberry")
        # Go to cart by click on button
        #scroll down
        self.driver.execute_script("window.scrollBy(500,0);")
        # sp.scroll()
        #Go to cart page and click on checkout button
        # co=checkout_page(self.driver)
        self.co.check_out()
        #compare message with success message
        ut=utils(self.driver)
        ut.assert_success("Success! Thank you!")
