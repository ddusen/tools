# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re

import redis


class RedisClient(object):
    conf = None

    """docstring for RedisClient"""

    def __init__(self, conf):
        self.conf = re.match(
            r"redis://(?P<host>.+):(?P<port>\d+)/(?P<db>.+)", conf).groupdict()

    def connect(self):
        pool = redis.ConnectionPool(
            host=self.conf['host'],
            port=self.conf['port'], db=self.conf['db'])
        return redis.Redis(connection_pool=pool)


def get_instance(conf):
    return RedisClient(conf).connect()


class RedisQueryApi(object):
    """Redis Query Api"""
    instance = None

    def __init__(self, conf):
        self.instance = get_instance(conf)

    def rpop(self, name):
        return self.instance.rpop(name)

    def delete(self, name):
        return self.instance.delete(name)

    def lindex(self, name, index):
        return self.instance.lindex(name, index)

    def llen(self, name):
        return self.instance.llen(name)

    def lpush(self, name, values):
        return self.instance.lpush(name, values)

    def lrange(self, name, start, end):
        return self.instance.lrange(name, start, end)

    def hset(self, name, url, value):
        self.instance.hset(name, url, value)

    def hget(self, name, url):
        return self.instance.hget(name, url)

    def hgetall(self, name):
        return self.instance.hgetall(name)

    def hexists(self, name, url):
        return self.instance.hexists(name, url)

    def scard(self, name):
        return self.instance.scard(name)

    def sort(self, name, start=None, num=None, by=None, get=None, desc=False, alpha=False, store=None):
        return self.instance.sort(name, start, num, by, get, desc, alpha, store)

    def set(self, url, value):
        return self.instance.set(url, value)

    def get(self, url):
        return self.instance.get(url)

    def expire(self, url, value):
        return self.instance.expire(url, value)

    def urls(self, url):
        return self.instance.urls(url)