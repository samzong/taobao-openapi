'''
Created by auto_sdk on 2020.04.08
'''
from top.api.base import RestApi
class WdtJbsStatSalesSummaryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.spec_id = None
		self.start_date = None
		self.warehouse_id = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.jbs.stat.sales.summary'
