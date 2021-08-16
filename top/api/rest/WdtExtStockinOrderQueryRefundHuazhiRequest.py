'''
Created by auto_sdk on 2021.04.20
'''
from top.api.base import RestApi
class WdtExtStockinOrderQueryRefundHuazhiRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.page_no = None
		self.page_size = None
		self.prop2 = None
		self.shop_no = None
		self.sid = None
		self.src_order_no = None
		self.start_time = None
		self.status = None
		self.stockin_no = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ext.stockin.order.query.refund.huazhi'
