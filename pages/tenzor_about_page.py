from pages.base_page import BasePage

block_working_selector = ("class name", "tensor_ru-container.tensor_ru-section.tensor_ru-About__block3")
block_working_images_selector = ("class name", "tensor_ru-About__block3-image-wrapper")

class TenzorAboutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://tensor.ru/about")

    def block_working(self):
        return self.find(block_working_selector)

    def block_working_is_displayed(self):
        return self.block_power_in_people().is_displayed()

    def block_working_images(self):
        return self.find_elements(block_working_images_selector)

