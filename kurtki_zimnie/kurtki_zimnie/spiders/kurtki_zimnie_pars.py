import scrapy
import csv

class KurtkiZimnieparsSpider(scrapy.Spider):
    name = "kurtki_zimnie_pars"
    allowed_domains = ["sudar.su"]
    start_urls = ["https://sudar.su/catalog/kurtki_zimnie/"]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8-sig',  # Устанавливаем кодировку для записи CSV
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'kurtki.csv',
        'FEED_OVERWRITE': True  # Перезаписываем файл при каждом запуске
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

        # Пагинация
        next_page_button = response.css('div.btn.btn-default.btn-lg.center-block[data-use="show-more-2"]')
        if next_page_button:
            next_page_url = response.urljoin(next_page_button.attrib.get('data-url', ''))
            if next_page_url:
                yield scrapy.Request(next_page_url, callback=self.parse)
