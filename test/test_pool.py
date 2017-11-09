from webdriver_pool.webdriver_pool import WebdriverPool
from webdriver_pool.webdriver_pool_config import WebDriverPoolConfig

if __name__ == "__main__":
    wdp_config = WebDriverPoolConfig(phantomjs_path="D:/program/phantomjs-2.1.1-windows/bin/phantomjs.exe")
    wd = WebdriverPool(wdp_config)
    driver = wd.acquire()
    driver.get("www.baidu.com")
    wd.release(driver)
    wd.stop()
    print(wd.acquire() is None)
