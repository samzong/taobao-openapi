'''
Created by auto_sdk on 2020.05.15
'''
from top.api.base import RestApi
class MiniapppTemplateInstantiateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.clients = None
		self.description = None
		self.ext_json = None
		self.icon = None
		self.name = None
		self.template_id = None
		self.template_version = None

	def getapiname(self):
		return 'taobao.miniappp.template.instantiate'
