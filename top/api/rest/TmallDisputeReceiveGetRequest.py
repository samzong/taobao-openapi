'''
Created by auto_sdk on 2019.07.24
'''
from top.api.base import RestApi
class TmallDisputeReceiveGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.end_modified = None
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.refund_id = None
		self.start_modified = None
		self.status = None
		self.type = None
		self.use_has_next = None

	def getapiname(self):
		return 'tmall.dispute.receive.get'
