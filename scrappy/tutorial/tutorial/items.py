import scrapy


class Platform(scrapy.Item):
    platform_name = scrapy.Field()
    agrement = scrapy.Field()


class Promoter(scrapy.Item):
    promoter_name = scrapy.Field()


class Project(scrapy.Item):
    project_name = scrapy.Field()
    platform_name = scrapy.Field()
    promoter_name = scrapy.Field()
    collected_amount = scrapy.Field()
    status = scrapy.Field()
    project_link = scrapy.Field()
