# -*- coding=utf-8 -*-
from pyzabbix import ZabbixAPI, ZabbixAPIException

class HostGroup(object):
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password
        self.client = ZabbixAPI(url=url, user=user, password=password)
        
    def get_all_hostgroup(self):
        params = {
            'ouput':'extend'
        }
        try:
            hostgroups = self.client.hostgroup.get(**params)
            if hostgroups:
                return hostgroups
            else:
                return None
        except Exception,e:
            return None
            
    def get_field_hostgroup(self,field):
        params = {
            'ouput':'extend'
        }
        params.update(field)
        try:
            hostgroups = self.client.hostgroup.get(**params)
            if hostgroups:
                return hostgroups
            else:
                return None
        except Exception,e:
            return None
            
    def create_hostgroup(self,params):
        try:
            hostgroups = self.client.hostgroup.create(**params)
            if hostgroups:
                return hostgroups
            else:
                return None
        except Exception,e:
            return None
            
    def mass_add_hostgroup(self,groups,field={}):
        params = {
            'groups':groups
        }
        params.update(field)
        try:
            hostgroups = self.client.hostgroup.massadd(**params)
            if hostgroups:
                return hostgroups
            else:
                return None
        except Exception,e:
            return None
            
    def update_hostgroup(self,groupid,new_hostgroup):
        params = {
            'groupid':groupid
        }
        params.update(new_hostgroup)
        try:
            hostgroups = self.client.hostgroup.update(**params)
            if hostgroups:
                return hostgroups
            else:
                return None
        except Exception,e:
            return None
            
    def update_mass_hostgroup(self,groups,new_hostgroup):
        params = {
            'groups':groups
        }
        params.update(new_hostgroup)
        try:
            hostgroups = self.client.hostgroup.massupdate(**params)
            if hostgroups:
                return hostgroups
            else:
                return None
        except Exception,e:
            return None
            
    def delete_hostgroup(self,hostgroupids):
        params = hostgroupids
        try:
            actions = self.client.hostgroup.delete(**params)
            if actions:
                return actions
            else:
                return None
        except Exception,e:
            return None
            
    def delete_mass_hostgroup(self,groupids,field={}):
        params = {
            'groupids':groupids
        }
        params.update(field)
        try:
            hostgroups = self.client.hostgroup.field(**params)
            if hostgroups:
                return hostgroups
            else:
                return None
        except Exception,e:
            return None