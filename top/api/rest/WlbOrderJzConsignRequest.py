'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi
class WlbOrderJzConsignRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ins_receiver_to = None
		self.ins_tp_dto = None
		self.jz_receiver_to = None
		self.jz_top_args = None
		self.lg_tp_dto = None
		self.sender_id = None
		self.tid = None

	def getapiname(self):
		return 'taobao.wlb.order.jz.consign'
