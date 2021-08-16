'''
Created by auto_sdk on 2021.08.09
'''
from top.api.base import RestApi
class MiniappDistributionMaterialGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.material_request = None

	def getapiname(self):
		return 'taobao.miniapp.distribution.material.get'
