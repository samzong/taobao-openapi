'''
Created by auto_sdk on 2020.06.01
'''
from top.api.base import RestApi
class WdtVipApiRefundQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.platform_id = None
		self.refund_no = None
		self.shop_no = None
		self.sid = None
		self.start_time = None
		self.tid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.vip.api.refund.query'
