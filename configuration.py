# -*- coding=utf-8 -*-
from pyzabbix import ZabbixAPI, ZabbixAPIException

class Configuration(object):
    def __init__(self, url, user, password):
       self.url = url
       self.user = user
       self.password = password
       self.client = ZabbixAPI(url=url, user=user, password=password)
       
    def export_configuration(self,format='json',options={}):
        params = {
            'format':format,
            'options':options
        }
        try:
            configurations = self.client.configuration.export(**params)
            if configurations:
                return configurations
            else:
                return None
        except Exception,e:
            return None
            
    def import_configuration(self,format='json',source='',rules ={}):
        params = {
            'format':format,
            'source':source,
            'rules':rules
        }
        try:
            configurations = self.client.configuration.import(**params)
            if configurations:
                return configurations
            else:
                return None
        except Exception,e:
            return None