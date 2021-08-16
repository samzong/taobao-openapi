'''
Created by auto_sdk on 2020.07.17
'''
from top.api.base import RestApi
class WdtExtRefundSpecDayQueryPdecRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.refund_date = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ext.refund.spec.day.query.pdec'
