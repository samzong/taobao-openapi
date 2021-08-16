'''
Created by auto_sdk on 2021.06.07
'''
from top.api.base import RestApi
class WdtTradesStatusQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.sid = None
		self.tid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.trades.status.query'
