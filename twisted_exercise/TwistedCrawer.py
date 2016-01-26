# -*-coding: UTF-8 -*-
from twisted.internet import reactor
from twisted.web import client

def result(content):
    print content
    reactor.stop()

deferred = client.getPage('http://news.baidu.com')
deferred.addCallback(result)
reactor.run()