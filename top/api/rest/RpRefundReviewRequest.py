'''
Created by auto_sdk on 2018.07.27
'''
from top.api.base import RestApi
class RpRefundReviewRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.message = None
		self.operator = None
		self.refund_id = None
		self.refund_phase = None
		self.refund_version = None
		self.result = None

	def getapiname(self):
		return 'taobao.rp.refund.review'
