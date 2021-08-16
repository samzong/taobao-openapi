'''
Created by auto_sdk on 2020.11.05
'''
from top.api.base import RestApi
class WdtStockQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.barcode = None
		self.end_time = None
		self.goods_no = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.spec_no = None
		self.start_time = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stock.query'
