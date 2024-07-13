import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Viewer:
    def __init__(self, proxy, fingerprint):
        self.proxy = proxy
        self.fingerprint = fingerprint

    def setup_browser(self):
        options = Options()
        options.add_argument(f'--proxy-server={self.proxy}')
        options.add_argument(f"user-agent={self.fingerprint['user_agent']}")

        self.browser = webdriver.Chrome(options=options)

    def watch_video(self, url, duration):
        self.setup_browser()
        self.browser.get(url)
        time.sleep(duration)
        self.browser.quit()
