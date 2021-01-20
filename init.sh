ECHO 'creating database...'
python3 createDatabase.py
ECHO 'database succesfully created'
cd scrappy/tutorial
ECHO 'platform crawler deployed...'
scrapy crawl platform_crawler
ECHO 'platform crawler finished'
ECHO 'promoter crawler deployed...'
scrapy crawl promoter_crawler
ECHO 'promoter crawler finished'
ECHO 'project crawler deployed...'
scrapy crawl project_crawler
ECHO 'project crawler finished'