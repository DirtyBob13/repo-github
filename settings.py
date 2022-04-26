# Scrapy settings for jobparser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jobparser'
IMAGES_STORE = 'photos'

SPIDER_MODULES = ['jobparser.spiders']
NEWSPIDER_MODULE = 'jobparser.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#'cookie': 'abtest={"16":0,"19":1}; CACHED_FRONT_FORM_KEY=TZmOedRbArNx2alm; frontend=ba5u3i2rgq46e8860avrf1e5u9; frontend_cid=BfeVtSlxREuVQPr9; castorama_current_shop=54; store=default; reload_shop=1; t2s-analytics=63dec129-9eec-4a4b-b080-24c8917ee2de; t2s-p=63dec129-9eec-4a4b-b080-24c8917ee2de; rrpvid=250645692983378; custom_sessionId=1650290362864.ifhq17fs05; _gcl_au=1.1.1204313082.1650290363; _gid=GA1.2.506988786.1650290364; rcuid=5d3b88fa6bfc7d000162558c; _userGUID=0:l24s9u61:ycvtlOVgtwnle3qoIKGYaTHfWIEznthj; dSesn=c995a3de-59ca-5bf3-6435-7d90db6252a6; _dvs=0:l24s9u61:6DV3gRBvpfOs~~99TTtrMitjxV_XV2AK; _ym_d=1650290364; _ym_uid=1650290364649339606; _ym_visorc=b; _ym_isad=2; mgo_uid=iSG9BMDEHltWKcdk7NFL; adrdel=1; adrcid=ApE9bv8cHCZGj83SjcUHe5A; castorama_nearest_shop=blocked; CART=92e41a70b854a353c1cb30a78904fd43; CATEGORY_INFO=[]; LAST_CATEGORY=1706; VIEWED_PRODUCT_IDS=139477; _ga=GA1.2.691434663.1650290364; cto_bundle=HmFQkV9jWW5JV3haRFhOaElzNVN1bDhobXpoNVJGSCUyQlVNNGZLaW0lMkY0QlV6Slk5bVhVJTJCMVM4Q052enlPcnQwR1BiRGROQVZ1SDF5Z0lxM1RxQlF4ZkRaVHA4MlozVTdKN2M0a1NBUllJTmpCVkZBNjhmd2dOUXVoMHNBNWslMkZwUHEyY1V2YjVxRmtNcmtsZzUwSjY1T1lmZUxpdyUzRCUzRA; _ga_97D13X79QM=GS1.1.1650290362.1.1.1650290929.0; rr-testCookie=testvalue'
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jobparser.middlewares.JobparserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jobparser.middlewares.JobparserDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'jobparser.pipelines.JobparserPipeline': 300,
   'jobparser.pipelines.JobparserPhotosPipeline': 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
