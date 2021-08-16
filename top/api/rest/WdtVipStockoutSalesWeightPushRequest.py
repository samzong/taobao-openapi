'''
Created by auto_sdk on 2020.06.01
'''
from top.api.base import RestApi
class WdtVipStockoutSalesWeightPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.is_setting = None
		self.logistics_no = None
		self.packager_no = None
		self.sid = None
		self.weight = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.vip.stockout.sales.weight.push'
