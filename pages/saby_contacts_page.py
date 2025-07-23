from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

banner_tenzor_selector = ("xpath", '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
region_selector = ("xpath", '(//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"])[1]')
block_partners_selector = ("id", "contacts_list")
partners_selector = ("css selector", ".sbisru-Contacts-List__name")
kamchatka_selector = ("xpath", "//span[@class='sbis_ru-link' and @title='Камчатский край']")

class SabyContactsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://saby.ru/contacts/77-moskva?tab=clients")

    def banner_tenzor(self):
        return self.find(banner_tenzor_selector)

    def banner_tenzor_is_displayed(self):
        return self.banner_tenzor().is_displayed()

    def banner_tenzor_click(self):
        return self.banner_tenzor().click()

    def region(self):
        return self.find(region_selector)

    def region_text(self):
        return self.region().text

    def region_click(self):
        return self.region().click()

    def block_partners(self):
        return self.find(block_partners_selector)

    def partners(self):
        return self.find_elements(partners_selector)

    def partner_is_displayed(self):
        return self.block_partners().is_displayed()

    def partners_list(self):
        return [p.text for p in self.partners()]

    def kamchatka_region(self):
        return self.find(kamchatka_selector)

    def kamchatka_region_click(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(("xpath", "//span[@class='sbis_ru-link' and @title='Камчатский край']"))
        )
        self.browser.execute_script("arguments[0].click();", element)
        # Ожидание изменения URL
        WebDriverWait(self.browser, 10).until(
            EC.url_contains("kamchatskij-kraj")
        )
