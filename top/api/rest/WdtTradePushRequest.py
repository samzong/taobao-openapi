'''
Created by auto_sdk on 2020.12.04
'''
from top.api.base import RestApi
class WdtTradePushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.shop_no = None
		self.sid = None
		self.trade_list = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.trade.push'
