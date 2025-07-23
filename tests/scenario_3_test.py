import os

from conftest import browser
from pages.saby_page import SabyBasePage
from pages.download_local_page import DownloadPage

def test_download_local_version_is_exist(browser):
    page = SabyBasePage(browser=browser)
    page.open()
    assert page.local_version_is_displayed()

def test_download_local_version_click(browser):
    page = SabyBasePage(browser=browser)
    page.open()
    page.local_version_click()
    assert "saby.ru/download" in browser.current_url

def test_download_web_installer_is_exist(browser):
    page = DownloadPage(browser=browser)
    page.open()
    assert page.web_installer_saby_is_displayed()

def test_verify_size(browser):
    page = DownloadPage(browser=browser)
    page.open()
    page.delete_old_file("saby-setup.exe")
    page.web_installer_saby_click()
    page.wait_for_download("saby-setup.exe")
    expected_size = page.get_file_size_from_site()
    real_size = page.get_downloaded_file_size("saby-setup.exe")
    assert abs(real_size - expected_size) < 0.1, (
        f"Размер файла не совпадает: ожидалось {expected_size} МБ, "
        f"получено {real_size:.2f} МБ")