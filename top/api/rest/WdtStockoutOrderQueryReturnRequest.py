'''
Created by auto_sdk on 2021.08.11
'''
from top.api.base import RestApi
class WdtStockoutOrderQueryReturnRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.end_time = None
		self.outer_no = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.src_order_no = None
		self.start_time = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stockout.order.query.return'
