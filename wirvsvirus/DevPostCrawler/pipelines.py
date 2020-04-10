# -*- coding: utf-8 -*-

# Pipeline has to be added to ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from DevPostCrawler.language_processing import LanguageProcessing


class DevPostCrawlerPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'w')
        self.lp = LanguageProcessing()

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        dict_item = dict(item)

        # Extract most frequent words
        story_text = item['storyText'][0]
        dict_item['popularWords'] = self.lp.get_keyword(story_text)

        # Detect the subtitle language and translate it to english
        subtitle = item['subtitle'][0]
        language = self.lp.get_language(subtitle)
        dict_item['language'] = language

        if dict_item['language'] != 'english':
            dict_item['enSubtitle'] = self.lp.ggl_translate(subtitle)[0]
        else:
            dict_item['enSubtitle'] = ''

        line = json.dumps(dict_item) + "\n"
        self.file.write(line)
        return item
