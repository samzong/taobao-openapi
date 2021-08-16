'''
Created by auto_sdk on 2021.07.22
'''
from top.api.base import RestApi
class TradeFullinfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.include_oaid = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.fullinfo.get'
