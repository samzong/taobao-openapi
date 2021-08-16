'''
Created by auto_sdk on 2021.05.26
'''
from top.api.base import RestApi
class WdtRefundQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_rights = None
		self.appkey = None
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.process_status = None
		self.refund_no = None
		self.shop_no = None
		self.sid = None
		self.src_refund_no = None
		self.start_time = None
		self.tid = None
		self.time_type = None
		self.trade_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.refund.query'
