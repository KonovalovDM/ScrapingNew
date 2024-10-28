import scrapy
import csv

class KurtkiZimnieparsSpider(scrapy.Spider):
    name = "kurtki_zimnie_pars"
    allowed_domains = ["sudar.su"]
    start_urls = ["https://sudar.su/catalog/kurtki_zimnie/"]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8-sig'  # Устанавливаем кодировку для записи CSV
    }

    def parse(self, response):
        kurtki = response.css("div.col-md-12")

        for kurtka in kurtki:
            try:
                name = kurtka.css('div.b-card__title p::text').get()
                price = kurtka.css('div.b-price b::text').get()
                url = response.urljoin(kurtka.css('a').attrib['href'])

                yield {
                    'name': name,
                    'price': price,
                    'url': url
                }

            except Exception as e:
                self.logger.error("Произошла ошибка при парсинге данных: %s", e)
                continue
