'''
Created by auto_sdk on 2020.12.21
'''
from top.api.base import RestApi
class WdtTradeLogsQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.is_his = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.src_tids = None
		self.start_time = None
		self.trade_nos = None
		self.type = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.trade.logs.query'
