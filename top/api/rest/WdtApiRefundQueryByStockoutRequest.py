'''
Created by auto_sdk on 2018.01.27
'''
from top.api.base import RestApi
class WdtApiRefundQueryByStockoutRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.sid = None
		self.stockout_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.api.refund.query.by.stockout'
