'''
Created by auto_sdk on 2020.08.31
'''
from top.api.base import RestApi
class WdtPurchaseApplyPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.details_list = None
		self.employee_no = None
		self.expected_time = None
		self.is_submit = None
		self.remark = None
		self.sid = None
		self.warehouse_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.purchase.apply.push'
