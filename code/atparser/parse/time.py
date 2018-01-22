# -*- coding:utf8 -*-

def _time(page):
    return page[page.find("<p>Time Limit: ")+15:page.find(" sec / M")]
