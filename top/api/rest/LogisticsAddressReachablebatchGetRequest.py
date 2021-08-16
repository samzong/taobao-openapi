'''
Created by auto_sdk on 2021.01.26
'''
from top.api.base import RestApi
class LogisticsAddressReachablebatchGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.address_list = None

	def getapiname(self):
		return 'taobao.logistics.address.reachablebatch.get'
