"""
Use this to generate a list of filenames of those files returned by the suggested 
'hole punch' search on the LOC website identifying those images with possible holes
punched in their negative.

returns a FsaRecordUrl scrapy.item object

NOTE: The FsaRecordUrl item is fine for our purposes, but the item attribute 
'recordUrl' is maybe a little misleading title. It is suggested the final output csv
is modified so that this field name is removed or chnaged to something more 
appropriate

NOTE: run with below command:

   scrapy crawl fsa1935_holePunch -o [csvTitle].csv -t csv 2>&1 | tee [somelogfile]

"""

import scrapy
from LOC_FSA_1935.items import FsaRecordUrl
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class FSA_1935_Spider(scrapy.Spider):

    name = "fsa1935_holePunch"
    custom_settings = { 'FEED_FORMAT':'csv', }

    # custom options (use to adapt to future searches)
    query = '1935+hole+punch'
    page_length = 23

    # populate start_urls:
    start_urls = []
    urlForm = 'https://www.loc.gov/pictures/search/?q={}&amp;sp={}&amp;co=fsa'

    for i in range(1, page_length):
        start_urls.append(urlForm.format(query, i))

    def parse(self, response):
        record = FsaRecordUrl()
        itemResults = BeautifulSoup(response.text, 'lxml').find_all('a', 
                class_='preview')

        for url in itemResults:
            record['recordUrl'] = url['rel'][0].split('/')[-1].replace(
                    '_150px.jpg', '')
            yield record 
