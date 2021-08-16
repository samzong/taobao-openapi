'''
Created by auto_sdk on 2020.12.25
'''
from top.api.base import RestApi
class WdtStockInoutSnQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.order_no = None
		self.order_type = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.sn = None
		self.spec_no = None
		self.start_time = None
		self.sub_order_type = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stock.inout.sn.query'
