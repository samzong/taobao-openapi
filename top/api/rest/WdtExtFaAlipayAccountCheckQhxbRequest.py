'''
Created by auto_sdk on 2020.07.01
'''
from top.api.base import RestApi
class WdtExtFaAlipayAccountCheckQhxbRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.platform_id = None
		self.sid = None
		self.start_time = None
		self.status = None
		self.type = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ext.fa.alipay.account.check.qhxb'
