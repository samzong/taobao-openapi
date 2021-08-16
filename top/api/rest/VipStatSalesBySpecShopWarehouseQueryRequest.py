'''
Created by auto_sdk on 2020.06.29
'''
from top.api.base import RestApi
class VipStatSalesBySpecShopWarehouseQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_rights = None
		self.consign_date = None
		self.shop_no = None
		self.sid = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.vip.stat.sales.by.spec.shop.warehouse.query'
