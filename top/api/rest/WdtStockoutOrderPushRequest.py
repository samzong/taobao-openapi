'''
Created by auto_sdk on 2020.05.28
'''
from top.api.base import RestApi
class WdtStockoutOrderPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.sid = None
		self.stockout_info = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stockout.order.push'
