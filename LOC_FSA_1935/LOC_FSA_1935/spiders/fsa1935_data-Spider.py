# NOTE: run with below command:
#   scrapy crawl fsa1935_data -o [csvTitle].csv -t 2>&1 | tee [somelogfile]
"""
Use to create a csv of metadata associated with a series of records.

returns a csv of collated metadata IF the associated record has digitized images.
"""

import scrapy
from LOC_FSA_1935.items import FsaRecord
from bs4 import BeautifulSoup
import re
import csv
from urllib.parse import urljoin


class FSA_Spider(scrapy.Spider):

    name = "fsa1935_data"
    custom_settings = { 'FEED_FORMAT':'csv', }

    # populate start_urls:
    start_urls = []
    with open('fsa1935_links.csv', 'r', newline='') as csvFd:
        for url in csv.reader(csvFd):
            start_urls.append(url[0])
    csvFd.close()


    def parse(self, response):
        record = FsaRecord()
        record['recordUrl'] = response.url

        image = BeautifulSoup(response.text, 'lxml').find('link',
                type=['image/gif', 'image/jpg', 'image/tif'])

        if image:
            # populate FsaRecord fields
            head = BeautifulSoup(response.text, 'lxml').find('head')

            record['subjects'] = []
            record['descriptions'] = []

            # populate FsaRecord fields:
            title = head.find('meta', {'name':'dc.title'})
            if title:
                record['title'] = title['content']
            else:
                record['title'] = 'unknown'

            creator = head.find('meta', {'name':'dc.creator'})
            if creator:
                record['creator'] = creator['content']
            else:
                record['creator'] = 'unknown'

            date = head.find('meta', {'name':'dc.date'})
            if date:
                record['date'] = date['content']
            else:
                record['date'] = 'unknown'

            rights = head.find('meta', {'name':'dc.rights'})
            if rights:
                record['rights'] = rights['content']
            else:
                record['rights'] = 'unknown'

            # subjects
            for tag in head.find_all('meta', {'name':'dc.subject'}):
                record['subjects'].append(tag['content'])
            # descriptions
            for tag in head.find_all('meta', {'name':'description'}):
                record['descriptions'].append(tag['content'])

            # match to image title:
            if image['type'] == 'image/gif':
                record['digitalId'] = image['href'].split('/')[-1].replace(
                        '_150px.jpg', '')
            else:
                record['digitalId'] = re.sub('[a-z]\.(jpg)|(tif)', '', 
                    image['href'].split('/')[-1])
                        
        else:
            record['title'] = 'Image not Digitized'

        yield record
