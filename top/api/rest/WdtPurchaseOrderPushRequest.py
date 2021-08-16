'''
Created by auto_sdk on 2021.03.11
'''
from top.api.base import RestApi
class WdtPurchaseOrderPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.purchase_info = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.purchase.order.push'
