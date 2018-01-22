# -*- coding:utf8 -*-

def _memory(page):
    return page[page.find("Memory Limit: ")+14:page.find(" MB</p>")+3]
