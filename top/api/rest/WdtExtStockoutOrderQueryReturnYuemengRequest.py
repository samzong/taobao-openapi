'''
Created by auto_sdk on 2020.10.23
'''
from top.api.base import RestApi
class WdtExtStockoutOrderQueryReturnYuemengRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.src_order_no = None
		self.start_time = None
		self.status = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ext.stockout.order.query.return.yuemeng'
