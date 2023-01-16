DOWNLOADER_MIDDLEWARES = {
    'scrapy_browser.scrapy.middleware.SeleniumDownloaderMiddleware': 500,
    'scrapy.downloadermiddlewares.DownloaderMiddleware': None,
}