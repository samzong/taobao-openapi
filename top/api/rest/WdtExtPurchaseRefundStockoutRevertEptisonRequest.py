'''
Created by auto_sdk on 2020.10.28
'''
from top.api.base import RestApi
class WdtExtPurchaseRefundStockoutRevertEptisonRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.order_info = None
		self.order_type = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ext.purchase.refund.stockout.revert.eptison'
