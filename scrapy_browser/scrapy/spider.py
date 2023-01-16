import scrapy
from scrapy import Request
from selenium import webdriver

from scrapy_browser.scrapy.http import SeleniumResponse


class SeleniumSpider(scrapy.Spider):
    name = 'SeleniumSpider'

    def start_requests(self):
        return [
            Request(
                url='https://www.google.ru/?q=123&gws_rd=ssl',
            )
        ]

    def parse(self, response, **kwargs):
        response: SeleniumResponse
        response.browser: webdriver.Firefox
        print(response.browser.page_source)
        pass