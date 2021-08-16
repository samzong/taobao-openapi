'''
Created by auto_sdk on 2021.05.18
'''
from top.api.base import RestApi
class MiniappDistributionOrderGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.order_id_request = None

	def getapiname(self):
		return 'taobao.miniapp.distribution.order.get'
