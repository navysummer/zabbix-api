# -*- coding=utf-8 -*-
from pyzabbix import ZabbixAPI, ZabbixAPIException

class Action(object):
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password
        self.client = ZabbixAPI(url=url, user=user, password=password)
        
    def get_all_action(self):
        params = {
            'ouput':'extend'
        }
        try:
            actions = self.client.drule.get(**params)
            if actions:
                return actions
            else:
                return None
        except Exception,e:
            return None
            
    def get_field_action(self,field):
        params = {
            'ouput':'extend'
        }
        params.update(field)
        try:
            actions = self.client.action.get(**params)
            if actions:
                return actions
            else:
                return None
        except Exception,e:
            return None
            
    def create_action(self,params):
        try:
            actions = self.client.action.create(**params)
            if actions:
                return actions
            else:
                return None
        except Exception,e:
            return None
            
    def update_action(self,actionid,new_action):
        params = {
            'actionid':actionid
        }
        params.update(new_action)
        try:
            actions = self.client.action.update(**params)
            if actions:
                return actions
            else:
                return None
        except Exception,e:
            return None
            
    def delete_action(self,actionids):
        params = actionids
        try:
            actions = self.client.action.delete(**params)
            if actions:
                return actions
            else:
                return None
        except Exception,e:
            return None