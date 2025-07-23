from pages.base_page import BasePage

power_in_people_selector = ("class name", "tensor_ru-Index__block4-content.tensor_ru-Index__card")
about_power_in_people_selector = ("xpath", "//div[contains(@class, 'tensor_ru-Index__block4-content tensor_ru-Index__card')]//a")

class TenzorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://tensor.ru/")

    def block_power_in_people(self):
        return self.find(power_in_people_selector)

    def block_power_in_people_is_displayed(self):
        return self.block_power_in_people().is_displayed()

    def about_power_in_people(self):
        return self.find(about_power_in_people_selector)

    def about_power_in_people_click(self):
        return self.about_power_in_people().click()