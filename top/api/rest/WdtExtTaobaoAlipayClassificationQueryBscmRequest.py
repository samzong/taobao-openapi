'''
Created by auto_sdk on 2020.05.19
'''
from top.api.base import RestApi
class WdtExtTaobaoAlipayClassificationQueryBscmRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.page_no = None
		self.page_size = None
		self.sid = None
		self.start_date = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ext.taobao.alipay.classification.query.bscm'
