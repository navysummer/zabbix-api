# -*- coding=utf-8 -*-
from pyzabbix import ZabbixAPI, ZabbixAPIException

class Drule(object):
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password
        self.client = ZabbixAPI(url=url, user=user, password=password)
    
    def get_all_rule(self):
        params = {
            'ouput':'extend',
            'selectDChecks': 'extend'
        }
        try:
            drules = self.client.drule.get(**params)
            if drules:
                return drules
            else:
                return None
        except Exception,e:
            return None
            
    def get_field_rule(self,field):
        params = {
            'ouput':'extend'
        }
        params.update(field)
        try:
            drules = self.client.drule.get(**params)
            if drules:
                return drules
            else:
                return None
        except Exception,e:
            return None
            
    def create_rule(self,dchecks,name='Zabbix agent discovery',iprange='192.168.1.1-255',status=0):
        params = {
            'name':name,
            'iprange':iprange,
            'dchecks':dchecks,
            'status'status
        }
        try:
            drules = self.client.drule.create(**params)
            if drules:
                return drules
            else:
                return None
        except Exception,e:
            return None
            
    def update_rule(self,druleid,new_rule)
        params = {
            'druleid':druleid
        }
        params.update(new_rule)
        try:
            drules = self.client.drule.update(**params)
            if drules:
                return drules
            else:
                return None
        except Exception,e:
            return None
            
    def delete_rule(self,rule_ids):
        params = rule_ids
        try:
            drules = self.client.drule.delete(**params)
            if drules:
                return drules
            else:
                return None
        except Exception,e:
            return None
            
    
        