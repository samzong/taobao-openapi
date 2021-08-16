'''
Created by auto_sdk on 2018.11.01
'''
from top.api.base import RestApi
class RpRefundsAgreeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.code = None
		self.refund_infos = None

	def getapiname(self):
		return 'taobao.rp.refunds.agree'
