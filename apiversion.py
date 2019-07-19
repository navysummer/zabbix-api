# -*- coding=utf-8 -*-
from pyzabbix import ZabbixAPI, ZabbixAPIException

class ApiVersion(object):
    def __init__(self, url, user, password):
       self.url = url
       self.user = user
       self.password = password
       self.client = ZabbixAPI(url=url, user=user, password=password)
       
    def get_version(self):
        params = []
        try:
            items = self.client.item.get(**params)
            if items:
                return items
            else:
                return None
        except Exception,e:
            return None