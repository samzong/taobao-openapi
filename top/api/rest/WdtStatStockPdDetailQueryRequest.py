'''
Created by auto_sdk on 2020.10.10
'''
from top.api.base import RestApi
class WdtStatStockPdDetailQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.pd_no = None
		self.sid = None
		self.start_time = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.stat.stock.pd.detail.query'
