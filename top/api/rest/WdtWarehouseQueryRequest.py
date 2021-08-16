'''
Created by auto_sdk on 2020.05.29
'''
from top.api.base import RestApi
class WdtWarehouseQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.end_time = None
		self.is_disabled = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.start_time = None
		self.warehouse_no = None
		self.warehouse_type = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.warehouse.query'
