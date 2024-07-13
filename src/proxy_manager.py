import random

class ProxyManager:
    def __init__(self, proxy_file):
        self.proxy_file = proxy_file
        self.proxies = self.load_proxies()

    def load_proxies(self):
        with open(self.proxy_file, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def get_random_proxy(self):
        return random.choice(self.proxies)
