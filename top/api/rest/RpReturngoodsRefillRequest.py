'''
Created by auto_sdk on 2018.07.27
'''
from top.api.base import RestApi
class RpReturngoodsRefillRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.logistics_company_code = None
		self.logistics_waybill_no = None
		self.refund_id = None
		self.refund_phase = None

	def getapiname(self):
		return 'taobao.rp.returngoods.refill'
