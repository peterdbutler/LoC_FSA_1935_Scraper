from csvLinkExtractor import urlExtract

urls = urlExtract('fsa1935_records.csv')
for i in range(0,10):
    print(urls[i])
