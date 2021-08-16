'''
Created by auto_sdk on 2021.02.26
'''
from top.api.base import RestApi
class WdtStockoutTransferPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.sid = None
		self.stockout_info = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stockout.transfer.push'
