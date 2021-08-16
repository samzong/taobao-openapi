'''
Created by auto_sdk on 2018.07.27
'''
from top.api.base import RestApi
class RpReturngoodsRefuseRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.refund_id = None
		self.refund_phase = None
		self.refund_version = None
		self.refuse_proof = None
		self.refuse_reason_id = None

	def getapiname(self):
		return 'taobao.rp.returngoods.refuse'

	def getMultipartParas(self):
		return ['refuse_proof']
