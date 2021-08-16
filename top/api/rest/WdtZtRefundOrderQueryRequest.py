'''
Created by auto_sdk on 2021.06.07
'''
from top.api.base import RestApi
class WdtZtRefundOrderQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.start_time = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.zt.refund.order.query'
