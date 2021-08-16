'''
Created by auto_sdk on 2020.05.29
'''
from top.api.base import RestApi
class WdtApiGoodsspecPushRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.api_goods_info = None
		self.appkey = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.api.goodsspec.push'
