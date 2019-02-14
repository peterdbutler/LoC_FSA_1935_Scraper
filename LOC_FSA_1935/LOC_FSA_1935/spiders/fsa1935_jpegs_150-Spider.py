# NOTE: run with below command:
#   scrapy crawl fsa1935_jpegs_150 -o [csvTitle].csv -t csv 2>&1 | tee [somelogfile]
"""
Spider built to scrape all jpeg images from LOC/FSA search '1935'
based around the search for '1935' (austensibly all images from 1935 in the 
collection

NOTE: pass url targets via a csv file, defined by the variable URL_TARGETS.
"""

import scrapy
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import csv

from LOC_FSA_1935.items import FsaImage

class FSA_Spider(scrapy.Spider):

    ####################      CUSTOM VARIABLES      ####################

    # change below variables to change how and where images are downloaded
    PIPELINE = { 'LOC_FSA_1935.pipelines.GetFsaImagesPipeline':1 }
    DESTINATION = '/media/pete/128gb_ExFAT/150px'

    # Variable to control csv file used for start_URLS
    URL_TARGETS = 'fsa1935_links.csv'

    ###################################################################

    name = "fsa1935_jpegs_150"
    custom_settings = { 
            'FEED_FORMAT' : 'csv', 
            'ITEM_PIPELINES' : PIPELINE,
            'IMAGES_STORE' : DESTINATION,
            'DOWNLOAD_DELAY' : 1
            }

    # populate start_urls:
    start_urls = []
    with open('fsa1935_links.csv', 'r', newline='') as csvFd:
        for url in csv.reader(csvFd):
            start_urls.append(url[0])
    csvFd.close()

    def parse(self, response):
        jpegs = BeautifulSoup(response.text, 'lxml').find_all('link',
                type=['image/gif']) 
        #NOTE: type='image/tif' # for tiffs
        image = FsaImage()
        image['recordUrl'] = response.url
        image['image_names'] = []
        image['image_urls'] = []
        for img in jpegs:
            image['image_names'].append(img['href'].split('/')[-1])
            image['image_urls'].append(urljoin(response.url, img['href']))
            yield image
