# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import json


def entityType_getter(response):
    for quote in response.css('div.page-resource-uri'):
        if quote.css('a::attr(href)').get() != "javascript:void()":
            yield {
                quote.css('a::attr(href)').get()
            }
        else:
            yield {
                'Thing'
            }


class QuotesSpider(scrapy.Spider):
    name = "dbpedia"
    urls = []

    def start_requests(self):
        for url in QuotesSpider.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for entity in entityType_getter(response):
            print("For:", response.url, "->  An Entity of Type:", entity)
