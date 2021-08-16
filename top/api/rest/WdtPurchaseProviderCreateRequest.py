'''
Created by auto_sdk on 2020.05.29
'''
from top.api.base import RestApi
class WdtPurchaseProviderCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.address = None
		self.appkey = None
		self.arrive_cycle_days = None
		self.charge_cycle_days = None
		self.contact = None
		self.email = None
		self.fax = None
		self.is_disabled = None
		self.last_purchase_time = None
		self.min_purchase_num = None
		self.mobile = None
		self.provider_name = None
		self.provider_no = None
		self.purchase_cycle_days = None
		self.qq = None
		self.remark = None
		self.sid = None
		self.telno = None
		self.wangwang = None
		self.website = None
		self.zip = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.purchase.provider.create'
