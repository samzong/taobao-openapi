'''
Created by auto_sdk on 2020.05.15
'''
from top.api.base import RestApi
class MiniappTemplateQueryappRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.page_num = None
		self.page_size = None
		self.template_id = None

	def getapiname(self):
		return 'taobao.miniapp.template.queryapp'
