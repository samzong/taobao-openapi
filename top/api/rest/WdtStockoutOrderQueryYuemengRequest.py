'''
Created by auto_sdk on 2020.07.22
'''
from top.api.base import RestApi
class WdtStockoutOrderQueryYuemengRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_rights = None
		self.end_time = None
		self.order_type = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.src_order_no = None
		self.start_time = None
		self.status = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stockout.order.query.yuemeng'
