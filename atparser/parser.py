# -*- coding:utf8 -*-

from exceptions.NotFoundException import *
from problem.problem import *
from parse import title,time,score,memory
import string, urllib2

PROBS = []
url = "https://beta.atcoder.jp/contests/{}/tasks/{}"

class Parser():
    def __init__(self, contest):
#        print "CREATE contest :",contest
        self.contest = contest
        self.run = True
        self.num = 1

    def parse(self):
        while self.run:
            try:
                contest_name = ("%s%03d" % (self.contest, self.num))
                for c in "abcdefghijklnmopqrstuvwxyz":
                    problem_code = contest_name + "_" + c
                    try:
                        _parse(contest_name, problem_code)
                    except NotFoundException as e:
                        continue
#                print self.num
                self.num += 1

            except NotFoundException as e:
                self.run = False

    def isRun(self):
        return self.run


def _parse(contest, code):
    try:
        now_url = url.format(contest, code)
        page = _get(now_url)
        prob = Problem(code, title._title(page), score._score(page), contest, url, time._time(page),memory._memory(page))
        PROBS.append(prob) # code, problem_name, score, contest_name, link, time_limit, memory_limit
        print "-"*50
        print "[*] check ",contest, code
        print prob
        print "-"*50
    except NotFoundException as e:
        pass

def _get(url):
    req = urllib2.Request(url)
    try:
        page = urllib2.urlopen(req).read()
    except urllib2.HTTPError as e:
        if "404" in str(e):
            raise NotFoundException


    return page
