from django.core.management import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy_browser.scrapy.spider import SeleniumSpider


class Command(BaseCommand):

    def handle(self, *args, **options):
        config = get_project_settings()
        process = CrawlerProcess(settings=config)

        process.crawl(SeleniumSpider)
        process.start()
