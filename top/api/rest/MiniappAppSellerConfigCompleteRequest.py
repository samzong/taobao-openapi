'''
Created by auto_sdk on 2021.06.15
'''
from top.api.base import RestApi
class MiniappAppSellerConfigCompleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_id = None
		self.version = None

	def getapiname(self):
		return 'taobao.miniapp.app.seller.config.complete'
