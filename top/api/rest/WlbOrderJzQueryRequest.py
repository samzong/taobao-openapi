'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi
class WlbOrderJzQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ins_jz_receiver_t_o = None
		self.jz_receiver_to = None
		self.sender_id = None
		self.tid = None

	def getapiname(self):
		return 'taobao.wlb.order.jz.query'
