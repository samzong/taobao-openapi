'''
Created by auto_sdk on 2021.08.13
'''
from top.api.base import RestApi
class WdtStockTransferPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.sid = None
		self.transfer_info = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stock.transfer.push'
