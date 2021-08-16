'''
Created by auto_sdk on 2018.10.12
'''
from top.api.base import RestApi
class OpenlinkSessionGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.code = None

	def getapiname(self):
		return 'taobao.openlink.session.get'
