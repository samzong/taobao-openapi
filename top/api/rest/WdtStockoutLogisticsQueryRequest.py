'''
Created by auto_sdk on 2021.03.15
'''
from top.api.base import RestApi
class WdtStockoutLogisticsQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.consign_time = None
		self.end_time = None
		self.get_time = None
		self.logistics_name = None
		self.logistics_no = None
		self.page_no = None
		self.page_size = None
		self.shop_no = None
		self.sid = None
		self.start_time = None
		self.status = None
		self.trade_no = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stockout.logistics.query'
