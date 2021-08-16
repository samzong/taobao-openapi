'''
Created by auto_sdk on 2020.08.31
'''
from top.api.base import RestApi
class WdtPurchaseApplyQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.purchase_apply_no = None
		self.sid = None
		self.start_time = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.purchase.apply.query'
