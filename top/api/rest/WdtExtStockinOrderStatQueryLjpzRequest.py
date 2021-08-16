'''
Created by auto_sdk on 2021.04.12
'''
from top.api.base import RestApi
class WdtExtStockinOrderStatQueryLjpzRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.start_time = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ext.stockin.order.stat.query.ljpz'
