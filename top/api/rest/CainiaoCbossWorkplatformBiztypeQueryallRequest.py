'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi
class CainiaoCbossWorkplatformBiztypeQueryallRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.level = None
		self.trade_id = None

	def getapiname(self):
		return 'cainiao.cboss.workplatform.biztype.queryall'
