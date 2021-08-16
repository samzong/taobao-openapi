'''
Created by auto_sdk on 2020.09.01
'''
from top.api.base import RestApi
class WdtStatSalesBySpecShopWarehouseQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.consign_date = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stat.sales.by.spec.shop.warehouse.query'
