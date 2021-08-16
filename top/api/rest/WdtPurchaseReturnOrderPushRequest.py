'''
Created by auto_sdk on 2021.02.26
'''
from top.api.base import RestApi
class WdtPurchaseReturnOrderPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.purchase_return_info = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.purchase.return.order.push'
