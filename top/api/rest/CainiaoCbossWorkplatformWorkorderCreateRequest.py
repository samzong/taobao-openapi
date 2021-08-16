'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi
class CainiaoCbossWorkplatformWorkorderCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.attach_path_list = None
		self.biz_entity_value = None
		self.biz_type = None
		self.creator_id = None
		self.creator_role = None
		self.features = None
		self.mail_no = None
		self.member_id = None
		self.member_role = None
		self.memo = None
		self.shop_user_id = None
		self.source = None
		self.source_sign = None
		self.trade_id = None
		self.work_order_type = None

	def getapiname(self):
		return 'cainiao.cboss.workplatform.workorder.create'
