import scrapy
from scrapy.pipelines.images import ImagesPipeline
import re
from PIL import Image
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO


class GetFsaImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for i,url in enumerate(item['image_urls']):
            image_name = item['image_names'][i]
            yield scrapy.Request(url, meta={'image_name': image_name})

    def file_path(self, request, response=None, info=None):
        return request.meta['image_name']

    def get_images(self, response, request, info):
        path = self.file_path(request, response=response, info=info)
        image = Image.open(BytesIO(response.body))
        buf = BytesIO()

        ext = response.url.split('.')[-1]
        if ext == 'tif':
            exif = image.tag_v2
            image.save(buf, 'TIFF', tiffinfo=exif) 
        else:
            image.save(buf, 'JPEG')

        yield path, image, buf
    
    """
    def get_images(self, response, request, info):
        path = self.file_path(request, response=response, info=info)
        image = Image.open(BytesIO(response.body))
        buf = BytesIO()

        ext = response.url.split('.')[-1]
        #if ext == re.compile('[Tt][Ii][Ff]{1,2}'):
        #    image.save(buf, 'TIFF', mode=image.mode)
        if ext == 'tif':
            image.save(buf, 'TIFF') 
        else:
            image.save(buf, 'JPEG')

        yield path, image, buf
    """
