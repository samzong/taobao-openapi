'''
Created by auto_sdk on 2020.06.01
'''
from top.api.base import RestApi
class WdtVipStockOutsideWmsQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.order_no = None
		self.order_type = None
		self.outer_no = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.start_time = None
		self.status = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.vip.stock.outside.wms.query'
