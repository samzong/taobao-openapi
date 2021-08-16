'''
Created by auto_sdk on 2021.08.11
'''
from top.api.base import RestApi
class TmallTraderateFeedsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.child_trade_id = None

	def getapiname(self):
		return 'tmall.traderate.feeds.get'
