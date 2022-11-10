import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for filme in response.css('.titleColumn'):
            yield {
                'titulo': filme.css('.titleColumn a::text').get(),
                'ano': filme.css('.secondaryInfo::text').get(),
                'nota': response.css('strong::text').get()
            }
