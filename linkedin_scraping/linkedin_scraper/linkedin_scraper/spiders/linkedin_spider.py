import scrapy
import pandas as pd
from scrapy.http import Request
from scrapy.signals import spider_closed

class LinkedinSpider(scrapy.Spider):
    name = 'linkedin_spider'
    start_urls = []
    crawled_data = []

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 3  # Set a delay of 5 seconds between requests
    }

    def __init__(self, *args, **kwargs):

        def add_prefix(link):
            if link[0] == 'w':
                return "https://" + link
            else:
                return link

        super(LinkedinSpider, self).__init__(*args, **kwargs)
        input_file = kwargs.get('input_file', None)
        if input_file:
            with open(input_file) as f:
                urls = [add_prefix(url) for url in f.readlines()]
                self.start_urls = [url.strip() for url in urls]
        else:
            raise ValueError('No input_file provided.')

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        summary_box = response.css("section.top-card-layout")
        name = summary_box.css("h1::text").get()
        headline = summary_box.css("h2::text").get()
        
        experience = response.xpath('//section[@id="experience-section"]/ul')

        # Find the 'li' tag and the 'a' tag within it
        a_tag = experience.xpath('.//div/a')

        # Extract job title, company name, joining date, and employment duration
        job_title = a_tag.xpath('.//h3/text()').get()
        current_company = a_tag.xpath('.//p[2]/text()').get()
        joining_date = a_tag.xpath('.//h4[1]/span[2]/text()').get()
        employment_duration = a_tag.xpath('.//h4[2]/span[2]/text()').get()

        



        scraped_data = {
            'name': name.strip() if name else '',
            'headline': headline.strip() if headline else '',
            'current_company': current_company.strip() if current_company else '',
        }

        self.crawled_data.append(scraped_data)
        yield scraped_data

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(LinkedinSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.export_to_excel, signal=spider_closed)
        return spider

    def export_to_excel(self):
        df = pd.DataFrame(self.crawled_data)
        df.to_excel('linkedin_profiles.xlsx', index=False)

