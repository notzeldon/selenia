from scrapy.http import Response


class SeleniumResponse(Response):

    def __init__(self, url, browser, *args, **kwargs):
        self.browser = browser
        super().__init__(url, *args, **kwargs)