'''
Created by auto_sdk on 2020.12.17
'''
from top.api.base import RestApi
class MiniappTemplateUpdateappRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.alias = None
		self.app_id = None
		self.clients = None
		self.desc = None
		self.ext_json = None
		self.icon = None
		self.template_id = None
		self.template_version = None

	def getapiname(self):
		return 'taobao.miniapp.template.updateapp'
