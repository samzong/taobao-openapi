'''
Created by auto_sdk on 2018.11.13
'''
from top.api.base import RestApi
class JushitaJdpUserAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.history_days = None
		self.host_ip = None
		self.host_name = None
		self.rds_name = None
		self.topics = None

	def getapiname(self):
		return 'taobao.jushita.jdp.user.add'
