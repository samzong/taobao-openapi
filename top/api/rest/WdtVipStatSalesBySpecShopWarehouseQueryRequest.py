'''
Created by auto_sdk on 2020.09.29
'''
from top.api.base import RestApi
class WdtVipStatSalesBySpecShopWarehouseQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_rights = None
		self.consign_date = None
		self.shop_no = None
		self.sid = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.vip.stat.sales.by.spec.shop.warehouse.query'
