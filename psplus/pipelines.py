# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from hashlib import shake_256

from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class PsplusPipeline:
    def process_item(self, item, spider):
        return item


class PsPlusImagesPipeline(ImagesPipeline):
    # Override the file_path method to customize the image file names
    def file_path(self, request, response=None, info=None, *, item=None):
        # The index [5:] in the super method is there to trim the beginning
        # with folder full/
        return (
            f"{item['unique_prefix']}_{super().file_path(request, response, info)[5:]}"
        )


class PsStorePipeline(ImagesPipeline):
    # Override the file_path method to customize the image file names
    def file_path(self, request, response=None, info=None, *, item=None):
        return f"{item['title']}_{super().file_path(request, response, info)[5:]}"
