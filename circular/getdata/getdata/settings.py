# Scrapy settings for getdata project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import os
PROJECT_ROOT = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )
sys.path.append(PROJECT_ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weeklycircular.settings")

BOT_NAME = 'getdata'

SPIDER_MODULES = ['getdata.spiders']
NEWSPIDER_MODULE = 'getdata.spiders'

ITEM_PIPELINES = {
        'getdata.pipelines.GetdataProductPipeline': 100,
        'getdata.pipelines.GetdataStorePipeline': 200,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'getdata (+http://www.yourdomain.com)'