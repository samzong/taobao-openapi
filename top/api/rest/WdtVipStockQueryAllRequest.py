'''
Created by auto_sdk on 2020.04.08
'''
from top.api.base import RestApi
class WdtVipStockQueryAllRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.vip.stock.query.all'
