'''
Created by auto_sdk on 2021.02.24
'''
from top.api.base import RestApi
class MiniappCloudFunctionInvokeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.data = None
		self.env = None
		self.exts = None
		self.handler = None
		self.name = None

	def getapiname(self):
		return 'taobao.miniapp.cloud.function.invoke'
