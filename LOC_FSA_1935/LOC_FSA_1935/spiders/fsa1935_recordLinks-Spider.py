# NOTE: run with below command:
#   scrapy crawl fsa1935_recordLinks -o [csvTitle].csv -t 2>&1 | tee [somelogfile]
"""
use this to generate a list of urls assocated with a search of the LOC/FSA domain

returns a full list of urls associated with each record found for a search of the
term '1935' at the LOC/FSA domain.

use to generate a csv or txt document of all image records under search.
"""

import scrapy
from LOC_FSA_1935.items import FsaRecordUrl
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class FSA_1935_Spider(scrapy.Spider):

    name = "fsa1935_recordLinks"
    custom_settings = { 'FEED_FORMAT':'csv', }

    # custom options (use to adapt to future searches)
    query = '1935'
    #TODO: figure out a good way to find a variable for search length, instead of
    #      using a number

    # populate start_urls:
    start_urls = []
    urlForm = 'https://www.loc.gov/pictures/search/?q={}&amp;sp={}&amp;co=fsa'
    # NOTE: 2653 is the number of results returned
    for i in range(1, 2654):
        start_urls.append(urlForm.format(query, i))

    def parse(self, response):
        # navigate to search results page 1
        record = FsaRecordUrl()
        itemResults = BeautifulSoup(response.text, 'lxml').find_all('div', 
                class_='result_item')
        for url in itemResults:
            record['recordUrl'] = urljoin(response.url, url.a['href'])
            yield record 
