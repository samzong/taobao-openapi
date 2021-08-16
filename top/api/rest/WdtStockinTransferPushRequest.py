'''
Created by auto_sdk on 2021.04.22
'''
from top.api.base import RestApi
class WdtStockinTransferPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.sid = None
		self.stockin_info = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stockin.transfer.push'
