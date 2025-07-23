from pages.saby_contacts_page import SabyContactsPage
from pages.saby_page import SabyBasePage

def test_section_contacts_is_exist(browser):
    page = SabyBasePage(browser=browser)
    page.open()
    assert page.section_contacts_is_displayed()

def test_section_contacts_more_office_click(browser):
    page = SabyBasePage(browser=browser)
    page.open()
    page.section_contacts_more_office_click()
    assert "contacts" in browser.current_url

def test_region_define(browser):
    page = SabyContactsPage(browser=browser)
    page.open()
    assert page.region_text() == "г. Москва"

def test_partner_is_exist(browser):
    page = SabyContactsPage(browser=browser)
    page.open()
    assert page.partner_is_displayed()

def test_change_region_to_Kamchatka(browser):
    page = SabyContactsPage(browser=browser)
    page.open()
    partners_list_before_change = page.partners_list()
    page.region_click()
    page.kamchatka_region_click()
    partners_list_after_change = page.partners_list()
    assert "Камчатский край" in browser.title, "title страницы после изменения не верен"
    assert "kamchatskij-kraj" in browser.current_url, "url страницы после изменения не верен"
    assert page.region_text() == "Камчатский край", "Неверный регион после изменения"
    assert partners_list_before_change != partners_list_after_change, "Список партнёров после изменения совпадает"
