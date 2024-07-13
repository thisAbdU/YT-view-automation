import unittest
from src.proxy_manager import ProxyManager
from src.fingerprint_manager import FingerprintManager

class TestBot(unittest.TestCase):
    def setUp(self):
        self.proxy_manager = ProxyManager('config/proxies.txt')
        self.fingerprint_manager = FingerprintManager()

    def test_proxy_loading(self):
        proxies = self.proxy_manager.load_proxies()
        self.assertTrue(len(proxies) > 0)

    def test_random_proxy(self):
        proxy = self.proxy_manager.get_random_proxy()
        self.assertIsNotNone(proxy)

    def test_random_fingerprint(self):
        fingerprint = self.fingerprint_manager.get_random_fingerprint()
        self.assertIsNotNone(fingerprint)

if __name__ == '__main__':
    unittest.main()
