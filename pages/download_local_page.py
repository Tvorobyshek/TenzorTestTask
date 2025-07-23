import os
import re
import time

from pages.base_page import BasePage

web_installer_saby_desktop_selector = ("xpath","//a[@href='https://update.saby.ru/SabyDesktop/master/win32/saby-setup.exe']")

class DownloadPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.download_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "downloads"))
    def open(self):
        self.browser.get("https://saby.ru/download?tab=plugin&innerTab=default")

    def web_installer_saby(self):
        return self.find(web_installer_saby_desktop_selector)

    def web_installer_saby_is_displayed(self):
        return self.web_installer_saby().is_displayed()

    def web_installer_saby_click(self):
        return self.web_installer_saby().click()

    def get_file_size_from_site(self):
        text = self.web_installer_saby().text
        match = re.search(r'(\d+\.\d+)\s*МБ', text)
        return float(match.group(1))

    def get_downloaded_file_size(self, filename):
        file_path = os.path.join(self.download_dir, filename)
        if os.path.exists(file_path):
            size_bytes = os.path.getsize(file_path)
            return size_bytes / (1024 * 1024)  # Перевод в мегабайты

    def wait_for_download(self, filename, timeout=30):
        start_time = time.time()
        file_path = os.path.join(self.download_dir, filename)
        while time.time() - start_time < timeout:
            if os.path.exists(file_path) and not file_path.endswith(".crdownload"):
                return True
            time.sleep(1)

    def delete_old_file(self, filename):
        file_path = os.path.join(self.download_dir, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
