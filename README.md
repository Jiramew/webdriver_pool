## Webdriver Pool - Selenium based webdriver pool

Webdriver Pool is library for building a pool of Webdriver when using Selenium.

Only running on python 3. Now only support Phantomjs.

Here is the demo code:
```python
from webdriver_pool.webdriver_pool import WebdriverPool
from webdriver_pool.webdriver_pool_config import WebDriverPoolConfig

wdp_config = WebDriverPoolConfig(phantomjs_path="D:/program/phantomjs-2.1.1-windows/bin/phantomjs.exe")
wd = WebdriverPool(wdp_config)
driver = wd.acquire()
driver.get("www.baidu.com")
wd.release(driver)
wd.stop()
print(wd.acquire() is None)
```

By using `acquire()` and `release()`, the time cost is reduced for getting a reusable Webdriver instance.

