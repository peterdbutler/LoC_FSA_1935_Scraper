BOT_NAME = 'LOC_FSA_1935'

SPIDER_MODULES = ['LOC_FSA_1935.spiders']
NEWSPIDER_MODULE = 'LOC_FSA_1935.spiders'

# Probably just for testing for now:
IMAGES_EXPIRES = 365

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# AUTOTHROTTLE (BE NICE!!)
AUTOTHROTTLE_ENABLED = True

MEDIA_ALLOW_REDIRECTS = False 

# Files Pipeline:
#ITEM_PIPELINES = {'LOC_FSA_1935.pipelines.GetFsaImagesPipeline':1}
#IMAGES_STORE = '/Volumes/FSA_IMAGES/1935/'

#DOWNLOAD_MAXSIZE = 3*1024*1024*1024     # 3316521912 = 3.221 GB
#DOWNLOAD_WARNSIZE = 1024*1024*1024      # 1073741824 = 1.074 GB
#DOWNLOAD_TIMEOUT = 600                  # 5 min
#DOWNLAOD_DELAY = 1

# for testing pipelines:
#IMAGES_STORE = '/Volumes/FSA_IMAGES/'
