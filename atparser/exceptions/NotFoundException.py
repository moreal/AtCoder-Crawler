# -*- coding:utf8 -*-

class NotFoundException(Exception):
    def __str__(self):
        return "This URL is wrongURL"

    def setMsg(self):
        self.msg = ""
        return self

    def getMsg(self):
        return self.msg
