'''
Created by auto_sdk on 2020.09.18
'''
from top.api.base import RestApi
class WdtPurchaseReturnPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.return_info = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.purchase.return.push'
