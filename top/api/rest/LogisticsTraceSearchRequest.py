'''
Created by auto_sdk on 2021.07.08
'''
from top.api.base import RestApi
class LogisticsTraceSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.is_split = None
		self.sub_tid = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.trace.search'
