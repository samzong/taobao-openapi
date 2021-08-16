'''
Created by auto_sdk on 2019.03.28
'''
from top.api.base import RestApi
class WdtAccountDetailQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.rec_id = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.account.detail.query'
