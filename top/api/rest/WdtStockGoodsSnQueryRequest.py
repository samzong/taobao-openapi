'''
Created by auto_sdk on 2020.12.25
'''
from top.api.base import RestApi
class WdtStockGoodsSnQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.goods_no = None
		self.sid = None
		self.sn = None
		self.spec_no = None
		self.src_order_no = None
		self.start_time = None
		self.status = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stock.goods.sn.query'
