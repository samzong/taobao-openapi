'''
Created by auto_sdk on 2020.06.01
'''
from top.api.base import RestApi
class WdtGoodsClassQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.class_name = None
		self.page_no = None
		self.page_size = None
		self.sid = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.goods.class.query'
