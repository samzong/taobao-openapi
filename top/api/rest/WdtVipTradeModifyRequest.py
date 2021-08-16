'''
Created by auto_sdk on 2020.12.25
'''
from top.api.base import RestApi
class WdtVipTradeModifyRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cs_remark = None
		self.flag_cover = None
		self.flag_name = None
		self.invoice_no = None
		self.logistics_code = None
		self.logistics_no = None
		self.print_remark = None
		self.remark_from = None
		self.sid = None
		self.trade_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.vip.trade.modify'
