# -*- coding:utf8 -*-

def _score(page):
    if page.find("<p>Score : <var>") == -1: return "No Score"
    return page[page.find("<p>Score : <var>")+16:page.find("</var> points</p>")]
