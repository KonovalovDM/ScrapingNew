import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8-sig'  # Устанавливаем кодировку для записи CSV
    }

    def parse(self, response):
        divans = response.css("div._Ud0k")
        for divan in divans:
            try:
                name = divan.css('div.lsooF span::text').get(),
                price = divan.css('div.pY3d2 span::text').get(),
                url = response.urljoin(divan.css('a').attrib['href'])

                yield {
                'name' : name,
                'price' : price,
                'url' : url
                }

            except Exception as e:
                self.logger.error("Произошла ошибка при парсинге данных: %s", e)
                continue
