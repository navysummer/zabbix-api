# -*- coding=utf-8 -*-
from pyzabbix import ZabbixAPI, ZabbixAPIException

class Item(object):
    def __init__(self, url, user, password):
       self.url = url
       self.user = user
       self.password = password
       self.client = ZabbixAPI(url=url, user=user, password=password)
       
    def get_all_item(self):
        params = {
            'ouput':'extend'
        }
        try:
            items = self.client.item.get(**params)
            if items:
                return items
            else:
                return None
        except Exception,e:
            return None
            
    def get_field_item(self,field):
        params = {
            'ouput':'extend'
        }
        params.update(field)
        try:
            items = self.client.item.get(**params)
            if items:
                return items
            else:
                return None
        except Exception,e:
            return None
            
    def create_item(self,field)
        params = {
            'ouput':'extend'
        }
        params.update(field)
        try:
            items = self.client.item.get(**params)
            if items:
                return items
            else:
                return None
        except Exception,e:
            return None
    
    def update_item(self,itemid,new_item):
        params = {
            'itemid':itemid
        }
        params.update(new_rule)
        try:
            items = self.client.item.update(**params)
            if items:
                return items
            else:
                return None
        except Exception,e:
            return None
            
    def delete_item(self,item_ids):
        params = item_ids
        try:
            items = self.client.item.delete(**params)
            if items:
                return items
            else:
                return None
        except Exception,e:
            return None