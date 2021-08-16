'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi
class FuwuScoresGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.current_page = None
		self.date = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.fuwu.scores.get'
