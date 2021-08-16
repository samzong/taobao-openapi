'''
Created by auto_sdk on 2020.12.03
'''
from top.api.base import RestApi
class WdtPurchaseProviderQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.column = None
		self.is_deleted = None
		self.page_no = None
		self.page_size = None
		self.provider_name = None
		self.provider_no = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.purchase.provider.query'
