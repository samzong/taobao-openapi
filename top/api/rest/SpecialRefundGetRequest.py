'''
Created by auto_sdk on 2020.06.09
'''
from top.api.base import RestApi
class SpecialRefundGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.refund_id = None

	def getapiname(self):
		return 'taobao.special.refund.get'
