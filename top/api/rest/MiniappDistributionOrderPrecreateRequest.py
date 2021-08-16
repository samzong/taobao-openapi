'''
Created by auto_sdk on 2021.08.10
'''
from top.api.base import RestApi
class MiniappDistributionOrderPrecreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.order_request = None

	def getapiname(self):
		return 'taobao.miniapp.distribution.order.precreate'
