'''
Created by auto_sdk on 2020.06.01
'''
from top.api.base import RestApi
class WdtRuinuanTradeLogsQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.src_tid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ruinuan.trade.logs.query'
