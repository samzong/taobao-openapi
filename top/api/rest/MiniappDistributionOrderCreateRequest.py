'''
Created by auto_sdk on 2021.07.29
'''
from top.api.base import RestApi
class MiniappDistributionOrderCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.order_request = None

	def getapiname(self):
		return 'taobao.miniapp.distribution.order.create'
