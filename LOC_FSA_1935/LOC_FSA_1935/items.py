import scrapy

class FsaImage(scrapy.Item):
    recordUrl = scrapy.Field()
    image_urls = scrapy.Field()
    image_names = scrapy.Field()
    image = scrapy.Field()

class FsaRecordUrl(scrapy.Item):
    recordUrl = scrapy.Field()

class FsaRecord(scrapy.Item):
    title = scrapy.Field() 
    creator = scrapy.Field()
    date = scrapy.Field()
    recordUrl = scrapy.Field()
    rights = scrapy.Field()
    digitalId = scrapy.Field()

    # NOTE: implement below as lists in spider 
    subjects = scrapy.Field()
    descriptions = scrapy.Field()




# NOTE: more or less depreciated. kept for backward compatibility...
class FsaData(scrapy.Item):
    title = scrapy.Field()
    digital_id = scrapy.Field()
    source_url = scrapy.Field()
    project = scrapy.Field()
    call_nums = scrapy.Field()
    next_url = scrapy.Field()
    img_sizes = scrapy.Field()
    img_names = scrapy.Field()
    img_urls = scrapy.Field()

class FsaImageData(scrapy.Item):
    title = scrapy.Field()
    digital_id = scrapy.Field()
    source_url = scrapy.Field()
    project = scrapy.Field()
    call_nums = scrapy.Field()
    next_url = scrapy.Field()
    image_sizes = scrapy.Field()
    image_names = scrapy.Field()

    # fields also used to download.
    image_urls = scrapy.Field()
    image = scrapy.Field()
