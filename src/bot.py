import time
import threading
from proxy_manager import ProxyManager
from fingerprint_manager import FingerprintManager
from viewer import Viewer
from config import settings

def start_viewing(url):
    proxy_manager = ProxyManager(settings.PROXY_FILE)
    fingerprint_manager = FingerprintManager()

    def run_viewer():
        proxy = proxy_manager.get_random_proxy()
        fingerprint = fingerprint_manager.get_random_fingerprint()
        viewer = Viewer(proxy, fingerprint)
        viewer.watch_video(url, settings.VIEW_DURATION)

    threads = []
    for _ in range(settings.MAX_THREADS):
        thread = threading.Thread(target=run_viewer)
        threads.append(thread)
        thread.start()
        time.sleep(settings.CYCLE_INTERVAL)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    start_viewing(video_url)
