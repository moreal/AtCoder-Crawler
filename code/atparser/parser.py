# -*- coding:utf8 -*-

from exceptions.NotFoundException import *
from problem.problem import *
from parse import title,time,score,memory
import string, urllib2

PROBS = []
url = "https://beta.atcoder.jp/contests/{}/tasks/{}"

class Parser():
    def __init__(self, contests):
        PROBS.append(Problem("code","problem_name","score","contest_name","link","time_limit","memory_limit"))
        self.contests = contests

    def parse(self):
        for contest in self.contests:

            self.num = 1

            while True:
                try:
                    contest_name = ("%s%03d" % (contest, self.num))
                    print "Find Contest", contest_name
                    _get("https://beta.atcoder.jp/contests/{}".format(contest_name))
                    for c in string.digits + string.ascii_lowercase:
                        problem_code = contest_name + "_" + c
                        try:
                            _parse(contest_name, problem_code)
                        except NotFoundException as e:
                            continue
                    self.num += 1

                except NotFoundException as e:
                    print "Error"
                    break

    def isRun(self):
        return self.run


def _parse(contest, code):
    try:
        now_url = url.format(contest, code)
        page = _get(now_url)
        prob = Problem(code, title._title(page), score._score(page), contest, now_url, time._time(page),memory._memory(page))
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
