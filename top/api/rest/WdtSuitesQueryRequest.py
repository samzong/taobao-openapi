'''
Created by auto_sdk on 2020.06.01
'''
from top.api.base import RestApi
class WdtSuitesQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.brand_name = None
		self.class_name = None
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.start_time = None
		self.suite_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.suites.query'
