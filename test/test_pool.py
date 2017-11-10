import time
from webdriver_pool.webdriver_pool import WebdriverPool
from webdriver_pool.webdriver_pool_config import WebDriverPoolConfig

if __name__ == "__main__":
    wdp_config = WebDriverPoolConfig(phantomjs_path="D:/program/phantomjs-2.1.1-windows/bin/phantomjs.exe")
    wd = WebdriverPool(wdp_config)
    for i in range(10):
        driver = wd.acquire()
        print(driver.session_id)
        driver.get("https://www.baidu.com")
        wd.release(driver)
        time.sleep(1)
    wd.stop()
    print(wd.acquire() is None)
