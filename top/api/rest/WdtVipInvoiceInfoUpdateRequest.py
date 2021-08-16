'''
Created by auto_sdk on 2020.11.09
'''
from top.api.base import RestApi
class WdtVipInvoiceInfoUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.error_info = None
		self.file_path = None
		self.invoice_code = None
		self.invoice_no = None
		self.sid = None
		self.status = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.vip.invoice.info.update'
