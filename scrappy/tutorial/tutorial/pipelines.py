import psycopg2
from psycopg2 import Error


class PlatformsPipeline(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect(host='localhost', user='root', password='root', dbname='test')
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into Platforms(platform_name,agrement) values(%s,%s)",
                         (item['platform_name'], item['agrement']))
        self.connection.commit()
        return item


class PromotersPipeline(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect(host='localhost', user='root', password='root', dbname='test')
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into Promoters(promoter_name) values(%s)",
                         (item['promoter_name'],))
        self.connection.commit()
        return item


class ProjectsPipeline(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect(host='localhost', user='root', password='root', dbname='test')
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("insert into Projects("
                             "project_name, platform_name, promoter_name, collected_amount,"
                             "status, project_link) "
                             "values(%s,%s,%s,%s,%s,%s)",
                             (item['project_name'],
                              item['platform_name'],
                              item['promoter_name'],
                              item['collected_amount'],
                              item['status'],
                              item['project_link']))
            self.connection.commit()
        except (Exception, Error) as error:
            print("Error while inserting project to PostgreSQL", error)
            self.connection.rollback()
        return item
