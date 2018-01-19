# -*- coding:utf8 -*-

def _title(page):
    return page[page.find("<title>")+7:page.find("</title>")]
