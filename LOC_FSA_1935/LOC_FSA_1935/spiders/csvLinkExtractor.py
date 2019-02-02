"""
csvLinkExtractor

use to open a csv of urls, extract each url, and return array of url strs
"""
import csv

def urlExtract(csvfile):
    urls = []
    with open(csvfile, mode='r', newline='') as csvfd:
        for url in csv.reader(csvfd):
            urls.append(url[0])
    csvfd.close()
    return urls
