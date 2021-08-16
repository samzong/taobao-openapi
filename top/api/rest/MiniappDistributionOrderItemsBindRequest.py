'''
Created by auto_sdk on 2021.03.17
'''
from top.api.base import RestApi
class MiniappDistributionOrderItemsBindRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.add_bind = None
		self.distribute_id = None
		self.target_entity_list = None

	def getapiname(self):
		return 'taobao.miniapp.distribution.order.items.bind'
