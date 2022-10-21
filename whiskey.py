# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 00:10:23 2022

@author: Jes Mary
"""
import scrapy

class whiskey(scrapy.Spider):
    name='whiskey'
    start_urls=["https://getlatka.com/"]
    
    def parse(self, response):
        for lista in response.css('a.directory_button__D1WeJ'):
            yield{
                'name': clientslist.css('a.saas-list_list_link__y_xyH').attrib['href']
                }
            