'''
Created by auto_sdk on 2020.12.28
'''
from top.api.base import RestApi
class WdtStockinQuickRefundPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.refund_list = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stockin.quick.refund.push'
