'''
Created by auto_sdk on 2020.07.21
'''
from top.api.base import RestApi
class ItemSkuGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.num_iid = None
		self.sku_id = None

	def getapiname(self):
		return 'taobao.item.sku.get'
