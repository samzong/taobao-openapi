'''
Created by auto_sdk on 2020.06.01
'''
from top.api.base import RestApi
class WdtStatRefundBySpecShopWarehouseQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.sid = None
		self.stockin_date = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stat.refund.by.spec.shop.warehouse.query'
