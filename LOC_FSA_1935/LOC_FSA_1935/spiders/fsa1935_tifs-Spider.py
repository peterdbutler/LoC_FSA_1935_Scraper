# NOTE: run with below command: 
#   scrapy crawl fsa1935_tifs -o [csvTitle].csv -t csv 2>&1 | tee [somelogfile]
"""
Spider built to scrape all tiff images from LOC/FSA search '1935'
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
    DESTINATION = '/Volumes/FSA_IMAGES/1935/'
    MAXSIZE = 3*1024*1024*1024      # 3316521912 (3.221 GB)
    WARNSIZE = 1024*1024*1024       # 1073741824 (1.074 GB)
    TIMEOUT = 600                   # 5 minutes
    DELAY = 1

    # Variable to control csv file used for start_URLS
    URL_TARGETS = 'fsa1935_links.csv'

    ###################################################################

    name = "fsa1935_tifs"
    custom_settings = { 
            'FEED_FORMAT'       : 'csv', 
            'ITEM_PIPELINES'    : PIPELINE,
            'IMAGES_STORE'      : DESTINATION,
            'DOWNLOAD_MAXSIZE'  : MAXSIZE,
            'DOWNLOAD_WARNSIZE' : WARNSIZE,
            'DOWNLOAD_TIMEOUT'  : TIMEOUT,
            'DOWNLOAD_DELAY'    : DELAY
            }

    # populate start_urls:
    start_urls = []
    with open(URL_TARGETS, 'r', newline='') as csvFd:
        for url in csv.reader(csvFd):
            start_urls.append(url[0])
    csvFd.close()

    def parse(self, response):
        tifs = BeautifulSoup(response.text, 'lxml').find_all('link',
                type='image/tif')
        image = FsaImage()
        image['recordUrl'] = response.url
        image['image_names'] = []
        image['image_urls'] = []
        for img in tifs:
            image['image_names'].append(img['href'].split('/')[-1])
            image['image_urls'].append(urljoin(response.url, img['href']))
            yield image
