from queue import Queue, Empty

from webdriver_pool.webdriver_item import WebDriverItem


class WebdriverPool(object):
    def __init__(self, config):
        self.config = config
        self.phantomjs_path = config.phantomjs_path
        self.all = Queue()
        self.available = Queue()
        self.stopped = False

    def acquire(self):
        if not self.stopped:
            try:
                return self.available.get_nowait()
            except Empty:
                driver_item = WebDriverItem(self.config)
                self.all.put(driver_item)
                return driver_item.get_webdriver()

    def release(self, driver_item):
        driver_item.delete_all_cookies()
        self.available.put(driver_item)

    def stop(self):
        self.stopped = True
        while True:
            try:
                driver_item = self.all.get(block=False)
                driver_item.get_webdriver().quit()
            except Empty:
                break
