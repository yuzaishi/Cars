# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ClubTopicReadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topic_id = scrapy.Field()  # 帖子ID
    reply = scrapy.Field()  # 回复帖子数
    view = scrapy.Field()  # 阅读数
    time = scrapy.Field()  # 采集时间

    def get_insert_sql(self):
        insert_sql = """insert into auto_home_club_topic_read (topic_id, reply, view, update_time) VALUES (%s, %s, %s ,str_to_date(%s,'%%Y-%%m-%%d') ) """
        params = (self["topic_id"], self["reply"], self["view"], self["time"])
        return insert_sql, params

    def distinct_data(self):
        query = """select id from auto_home_club_topic_read where id =%s"""
        params = (0)
        return query, params

