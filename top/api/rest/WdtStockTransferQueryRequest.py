'''
Created by auto_sdk on 2021.08.11
'''
from top.api.base import RestApi
class WdtStockTransferQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.api_outer_no = None
		self.appkey = None
		self.end_time = None
		self.from_warehouse_no = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.start_time = None
		self.status = None
		self.to_warehouse_no = None
		self.transfer_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stock.transfer.query'
