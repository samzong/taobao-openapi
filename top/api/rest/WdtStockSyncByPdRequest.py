'''
Created by auto_sdk on 2020.12.04
'''
from top.api.base import RestApi
class WdtStockSyncByPdRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.api_outer_no = None
		self.appkey = None
		self.goods_list = None
		self.is_check = None
		self.is_create_stock = None
		self.is_post_error = None
		self.mode = None
		self.sid = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stock.sync.by.pd'
