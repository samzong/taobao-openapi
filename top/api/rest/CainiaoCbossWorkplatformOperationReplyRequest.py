'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi
class CainiaoCbossWorkplatformOperationReplyRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.action_time = None
		self.action_type = None
		self.attach_path = None
		self.dealer_contact = None
		self.dealer_user_id = None
		self.features = None
		self.memo = None
		self.task_id = None
		self.work_order_id = None

	def getapiname(self):
		return 'cainiao.cboss.workplatform.operation.reply'
