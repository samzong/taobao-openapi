'''
Created by auto_sdk on 2020.10.12
'''
from top.api.base import RestApi
class MiniappShorturlCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.miniapp_url = None

	def getapiname(self):
		return 'taobao.miniapp.shorturl.create'
