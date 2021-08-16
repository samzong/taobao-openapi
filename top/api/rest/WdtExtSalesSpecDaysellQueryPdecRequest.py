'''
Created by auto_sdk on 2020.07.17
'''
from top.api.base import RestApi
class WdtExtSalesSpecDaysellQueryPdecRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.sales_date = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ext.sales.spec.daysell.query.pdec'
