'''
Created by auto_sdk on 2021.08.11
'''
from top.api.base import RestApi
class WdtStockPdOrderQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.api_outer_no = None
		self.app_rights = None
		self.appkey = None
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.pd_no = None
		self.sid = None
		self.start_time = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stock.pd.order.query'
