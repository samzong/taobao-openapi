'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi
class CainiaoCbossWorkplatformLogisticsIscainiaoorderRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.trade_id = None

	def getapiname(self):
		return 'cainiao.cboss.workplatform.logistics.iscainiaoorder'
