# -*- coding: utf-8 -*-

from __future__ import print_function

try:
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import Request, urlopen

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

import settings

#TODO:
# 1) len of proxies all and singular type
# 2) Comment method
# 3) implements errors


class FreeProxies(object):

    def __init__(self):
        # initial empty data
        self.data = {}
        self.refresh()

    def refresh(self):
        try:
            self.data = self.load_data()
        except:
            raise

    @staticmethod
    def _get_data(url):
        ua = UserAgent()
        proxies_req = Request(url)
        proxies_req.add_header('User-Agent', ua.random)
        proxies_doc = urlopen(proxies_req).read().decode('utf8')

        soup = BeautifulSoup(proxies_doc, 'html.parser')
        proxies_table = soup.find(id='proxylisttable')

        data = {}
        # Save proxies in the array
        for row in proxies_table.tbody.find_all('tr'):
            td = row.find_all('td')

            tp = td[4].string.replace('proxy', '').strip()

            if tp not in data:
                data[tp] = set()

            data[tp].add((td[0].string, td[1].string, bool(td[6].string), tp))

        return data

    @staticmethod
    def load_data():

        proxies = {}

        try:
            for url in settings.URLS:
                proxies.update(FreeProxies._get_data(url))
        except Exception as exc:
            raise

        return proxies

    def __getitem__(self, attr):
        return self.__getattr__(attr)

    def __getattr__(self, attr):

        try:
            if attr == 'random':
                proxies =  set().union(*self.data.values())
            else:
                proxies = self.data.get(attr, attr)

            return random.choice(list(proxies))

        except (KeyError, IndexError):
            raise

    @property
    def random_proxy(self):
        data = self.random
        protocol = 'https' if data[3] else 'http'
        ip, port = data[0], data[1]
        return "{}://{}:{}".format(protocol, ip, port)