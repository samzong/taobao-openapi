'''
Created by auto_sdk on 2020.06.01
'''
from top.api.base import RestApi
class WdtStatSalesSuitePerDayQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.mytest = None
		self.page_no = None
		self.page_size = None
		self.shop_no = None
		self.sid = None
		self.start_time = None
		self.suite_no = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stat.sales.suite.per.day.query'
