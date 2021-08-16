'''
Created by auto_sdk on 2019.01.03
'''
from top.api.base import RestApi
class MiniappUserInfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'taobao.miniapp.userInfo.get'
