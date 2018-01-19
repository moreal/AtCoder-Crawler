# -*- coding:utf8 -*-

class Problem:
    def __init__(self, code, problem_name, score, contest_name, link, time_limit, memory_limit):
        self.code = code
        self.problem_name = problem_name
        self.score = score
        self.contest_name = contest_name
        self.link = link
        self.time_limit = time_limit
        self.memory_limit = memory_limit

    def __str__(self):
        return '[ {} ] {} in "{}" / {} points'.format(self.code,self.problem_name,self.contest_name,self.score)
