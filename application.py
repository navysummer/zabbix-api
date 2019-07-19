# -*- coding=utf-8 -*-
from pyzabbix import ZabbixAPI, ZabbixAPIException

class Application(object):
    def __init__(self, url, user, password):
       self.url = url
       self.user = user
       self.password = password
       self.client = ZabbixAPI(url=url, user=user, password=password)
       
    def get_all_application(self):
        params = {
            'ouput':'extend'
        }
        try:
            applications = self.client.application.get(**params)
            if applications:
                return applications
            else:
                return None
        except Exception,e:
            return None
            
    def get_field_application(self,field):
        params = {
            'ouput':'extend'
        }
        params.update(field)
        try:
            applications = self.client.application.get(**params)
            if applications:
                return applications
            else:
                return None
        except Exception,e:
            return None
            
    def create_application(self,field):
        params = {
            'ouput':'extend'
        }
        params.update(field)
        try:
            applications = self.client.application.create(**params)
            if applications:
                return applications
            else:
                return None
        except Exception,e:
            return None
            
    def update_application(self,applicationid,new_application):
        params = {
            'applicationid':applicationid
        }
        params.update(new_application)
        try:
            applications = self.client.application.update(**params)
            if applications:
                return applications
            else:
                return None
        except Exception,e:
            return None
            
    def mass_add_application(self,applications,items={}):
        params = {
            'applications':applications
        }
        params.update(items)
        try:
            applications = self.client.application.massadd(**params)
            if applications:
                return applications
            else:
                return None
        except Exception,e:
            return None
            
    def delete_application(self,applicationids):
        params = applicationids
        try:
            applications = self.client.application.delete(**params)
            if applications:
                return applications
            else:
                return None
        except Exception,e:
            return None