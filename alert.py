# -*- coding=utf-8 -*-
from pyzabbix import ZabbixAPI, ZabbixAPIException

class Alert(object):
    def __init__(self, url, user, password):
       self.url = url
       self.user = user
       self.password = password
       self.client = ZabbixAPI(url=url, user=user, password=password)
       
    def get_all_alert(self):
        params = {
            'ouput':'extend'
        }
        try:
            alerts = self.client.alert.get(**params)
            if alerts:
                return alerts
            else:
                return None
        except Exception,e:
            return None
            
    def get_field_alert(self,field):
        params = {
            'ouput':'extend'
        }
        params.update(field)
        try:
            alerts = self.client.alert.get(**params)
            if alerts:
                return alerts
            else:
                return None
        except Exception,e:
            return None