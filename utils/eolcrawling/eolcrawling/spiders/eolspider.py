import logging
import json
import yaml
import os

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

logging.getLogger('scrapy').propagate = False

class EOLSpider(CrawlSpider):
    name = "eol"
    start_urls = ['https://endoflife.software/operating-systems/',]

    rules = (
        Rule(LinkExtractor(allow=('linux', )), callback='parse_item'),
        Rule(LinkExtractor(allow=('unix-like-bsd', )), callback='parse_item'),
        Rule(LinkExtractor(allow=('windows', )), callback='parse_item'),
    )


    def __init__(self):
        self.release_yaml = 'releases.yml'
        self.release_json = 'releases.json'
        try:
            os.remove(self.release_yaml)
            os.remove(self.release_json)
        except: pass

        super(EOLSpider, self).__init__()

    def parse_item(self, response):
        releases_index = {}

        for i,release in enumerate(response.xpath('//table[2]//thead//th/text()').getall()):
            releases_index[release] = i+1

        releases = {}
        tables = response.xpath('//table[2]//tr')
       
        for p in range(1,len(tables)):
            os_name = tables[p].xpath('td[1]/text()').extract_first()
            release_date = tables[p].xpath('td[{}]/text()'.format(releases_index['Release date'])).extract_first()
            end_date = tables[p].xpath('td[{}]/text()'.format(releases_index['End of life'])).extract_first()
       
            extended_support_table_num = releases_index.get('Extended Support', None)
            extended_support = None
            if extended_support_table_num is not None:
                extended_support = tables[p].xpath('td[{}]/text()'.format(extended_support_table_num)).extract_first()
       
            releases[tables[p].xpath('td[1]/text()').extract_first()] = {
                'release_date': release_date or '-',
                'end_date': end_date or '-',
                'extended_support': extended_support or '-'
            }


        if len(releases) > 0:
            yaml_dump = open(self.release_yaml, 'a')
            yaml_dump.write(yaml.dump(releases))
            yaml_dump.close()

            json_dump = open(self.release_json, 'a')
            json_dump.write(json.dumps(releases))
            json_dump.close()

            logging.info('[+] Dump finished! [+]')
