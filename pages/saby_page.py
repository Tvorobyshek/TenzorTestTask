from pages.base_page import BasePage

section_contacts_selector = ("xpath", "//div[contains(text(), 'Контакты')]")
section_contacts_more_office_selector = ("xpath", "//ul/li[2]//a[2]")
download_local_version_selector = ("xpath", "//a[contains(text(),'Скачать локальные версии')]")

class SabyBasePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://saby.ru")

    def section_contacts(self):
        return self.find(section_contacts_selector)

    def section_contacts_more_office(self):
        return self.find(section_contacts_more_office_selector)

    def section_contacts_is_displayed(self):
        return self.section_contacts().is_displayed()

    def section_contacts_more_office_click(self):
        self.section_contacts().click()
        return self.section_contacts_more_office().click()

    def local_version(self):
        return self.find(download_local_version_selector)

    def local_version_is_displayed(self):
        return self.local_version().is_displayed

    def local_version_click(self):
        return self.local_version().click()
