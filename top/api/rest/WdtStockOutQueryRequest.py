'''
Created by auto_sdk on 2020.10.16
'''
from top.api.base import RestApi
class WdtStockOutQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.except_type = None
		self.order_type = None
		self.page_no = None
		self.page_size = None
		self.search_type = None
		self.sid = None
		self.start_time = None
		self.status = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stock.out.query'
