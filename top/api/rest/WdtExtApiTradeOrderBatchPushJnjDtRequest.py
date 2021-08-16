'''
Created by auto_sdk on 2021.04.01
'''
from top.api.base import RestApi
class WdtExtApiTradeOrderBatchPushJnjDtRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.sid = None
		self.trade_list = None

	def getapiname(self):
		return 'hu3cgwt0tc.wdt.ext.api.trade.order.batch.push.jnj.dt'
