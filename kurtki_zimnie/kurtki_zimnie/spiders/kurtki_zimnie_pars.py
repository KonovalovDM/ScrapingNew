import scrapy


class KurtkiZimnieparsSpider(scrapy.Spider):
    name = "kurtki_zimnie_pars" #Указываем название
    allowed_domains = ["sudar.su"]  # Указываем только домен
    start_urls = ["https://sudar.su/catalog/kurtki_zimnie/"]

    def parse(self, response):
        kurtki = response.css("div.col-md-12")
        for kurtka in kurtki:
            yield {
                'name' : kurtka.css('div.b-card__title p::text').get(),
                'price' : kurtka.css('div.b-price b::text').get(),
                'url' : kurtka.css('a').attrib['href'] #Используем response.urljoin
            }