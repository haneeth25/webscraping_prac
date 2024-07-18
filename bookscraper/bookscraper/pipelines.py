# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        #Availability -> extract number of books- 
        string = adapter.get('availability')
        string = string[0]
        split_string = string.split('(')
        if len(split_string) <2:
            adapter['availability'] = 0
        else:
            av = split_string[1].split(' ')
            adapter['availability'] = int(av[0])
        return item
