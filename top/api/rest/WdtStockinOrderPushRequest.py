'''
Created by auto_sdk on 2020.12.04
'''
from top.api.base import RestApi
class WdtStockinOrderPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.sid = None
		self.stockin_info = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stockin.order.push'
