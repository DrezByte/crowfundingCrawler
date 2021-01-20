import scrapy
from psycopg2 import Error
from ..items import Platform, Promoter, Project


class PlatformSpider(scrapy.Spider):
    name = "platform_crawler"
    custom_settings = {'ITEM_PIPELINES': {'tutorial.pipelines.PlatformsPipeline': 800}}
    start_urls = ['https://www.hellocrowdfunding.com/immobilier/plateformes/']

    def parse(self, response):
        for tr in response.css('tbody.list tr'):
            platform_name = tr.css('a::text').extract_first()
            agrement = tr.css('td.status_date::text').extract_first()
            platform = Platform(platform_name=platform_name, agrement=agrement)
            yield platform


class PromoterSpider(scrapy.Spider):
    name = "promoter_crawler"
    custom_settings = {'ITEM_PIPELINES': {'tutorial.pipelines.PromotersPipeline': 800}}
    start_urls = ['https://www.hellocrowdfunding.com/immobilier/promoteurs/']

    def parse(self, response):
        for tr in response.css('tbody tr'):
            promoter_name = tr.css('a::text').extract_first()
            promoter = Promoter(promoter_name=promoter_name)
            yield promoter

        next_page = response.xpath("//li[contains(@class, 'page-item') and contains(.//a, '»')]/a/@href")[0].extract()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


class ProjectSpider(scrapy.Spider):
    name = "project_crawler"
    custom_settings = {'ITEM_PIPELINES': {'tutorial.pipelines.ProjectsPipeline': 800}}
    start_urls = ['https://www.hellocrowdfunding.com/immobilier/projets/']

    def parse(self, response):
        for next_page in response.xpath("//td[@class='name']/a/@href").extract():
            if next_page:
                yield response.follow(next_page, callback=self.parse_specific)


    def parse_specific(self, response):
        try:
            project_name = response.css('h1.text-custom::text').get().strip()
            status = response.css('ul.work_menu li')[0].css('span::text').get() or ''
            platform_name = response.css('ul.work_menu li')[1].css('a::text').get().strip()
            promoter_name = response.css('ul.work_menu li')[2].css('a::text').get().strip()
            project_link = response.css('ul.work_menu li')[3].xpath('a//@href').get() or ''

            project = Project(project_name=project_name,
                              platform_name=platform_name,
                              promoter_name=promoter_name,
                              collected_amount=100,
                              status=status,
                              project_link=project_link)
            yield project
        except (Exception, Error) as error:
            print("Error while inserting project to PostgreSQL", error)
