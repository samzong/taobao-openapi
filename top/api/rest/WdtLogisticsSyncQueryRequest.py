'''
Created by auto_sdk on 2020.05.28
'''
from top.api.base import RestApi
class WdtLogisticsSyncQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.appkey = None
		self.is_part_sync_able = None
		self.limit = None
		self.shop_no = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.logistics.sync.query'
