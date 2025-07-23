from pages.saby_page import SabyBasePage
from pages.saby_contacts_page import SabyContactsPage
from pages.tenzor_page import TenzorPage
from pages.tenzor_about_page import TenzorAboutPage

def test_section_contacts_is_exist(browser):
    page = SabyBasePage(browser=browser)
    page.open()
    assert page.section_contacts_is_displayed()

def test_section_contacts_more_office_click(browser):
    page = SabyBasePage(browser=browser)
    page.open()
    page.section_contacts_more_office_click()
    assert "contacts" in browser.current_url

def test_banner_tenzor_is_exist(browser):
    page = SabyContactsPage(browser=browser)
    page.open()
    assert page.banner_tenzor_is_displayed()

def test_banner_tenzor_click(browser):
    page = SabyContactsPage(browser=browser)
    page.open()
    page.banner_tenzor_click()
    tabs = browser.window_handles
    browser.switch_to.window(tabs[-1])
    assert "https://tensor.ru/" in browser.current_url

def test_power_in_people_is_exist(browser):
    page = TenzorPage(browser=browser)
    page.open()
    assert page.block_power_in_people_is_displayed()

def test_about_power_in_people_click(browser):
    page = TenzorPage(browser=browser)
    page.open()
    page.about_power_in_people_click()
    assert "https://tensor.ru/about" in browser.current_url

def test_images_width_height_same(browser):
    page = TenzorAboutPage(browser=browser)
    page.open()
    images = page.block_working_images()
    first_width = images[0].get_attribute("width")
    first_height = images[0].get_attribute("height")

    for img in images:
        width = img.get_attribute("width")
        height = img.get_attribute("height")
        assert width == first_width, f"Ширина {width} отличается от {first_width}"
        assert height == first_height, f"Высота {height} отличается от {first_height}"
