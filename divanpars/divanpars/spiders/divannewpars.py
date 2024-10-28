import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8-sig'  # Устанавливаем кодировку для записи CSV
    }

    def parse(self, response):
        svets = response.css("div.WdR1o")
        for svet in svets:
            try:
                name = svet.css('div.lsooF span::text').get(),
                price = svet.css('div.pY3d2 span::text').get(),
                url = response.urljoin(svet.css('a').attrib['href'])

                yield {
                'name' : name,
                'price' : price,
                'url' : url
                }

            except Exception as e:
                self.logger.error("Произошла ошибка при парсинге данных: %s", e)
                continue

