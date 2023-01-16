import time

from scrapy import signals
from selenium import webdriver

from scrapy_browser.scrapy.http import SeleniumResponse


class SeleniumDownloaderMiddleware:

    @classmethod
    def open_selenium(self, spider):
        if not hasattr(spider, '_browser'):
            browser = webdriver.Firefox()
            setattr(spider, '_browser', browser)

    @classmethod
    def browser(cls, spider):
        if hasattr(spider, '_browser'):
            browser = getattr(spider, '_browser')
            return browser


    @classmethod
    def close_selenium(self, spider):
        if hasattr(spider, '_browser'):
            browser = getattr(spider, '_browser')
            browser.close()

    @classmethod
    def from_crawler(cls, crawler):
        o = cls()
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
        return o

    def spider_opened(self, spider):
        self.open_selenium(spider)

    def spider_closed(self, spider):
        self.close_selenium(spider)

    def process_request(self, request, spider):
        browser = self.browser(spider)
        browser: webdriver.Firefox
        # https://stackoverflow.com/questions/15645093/setting-request-headers-in-selenium
        browser.get(request.url)
        return SeleniumResponse(request.url, browser, request=request)

    def process_response(self, request, response, spider):
        a = 1
        return response

    def process_exception(self, request, exception, spider):
        pass
