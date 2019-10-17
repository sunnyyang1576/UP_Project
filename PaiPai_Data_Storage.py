
class PaiPaiHFInstrument:
	"""
	HedgeFund which are using PaiPai information.
	"""

	def __init__(self, unique_id, fund_id):
		"""Initialize the Hedge Fund

		:param unique_id: int
		:param fund_id: str
		:param asset_size_storage: AssetSizeStorage
		:param nav: NavStorage
		:param personnel: PersonnelStorage
		:param strategy: StaticStorage
		:param attribute: StaticStorage
		"""

		self.unique_id = unique_id
		self.fund_id = fund_id


		self.store_list = []


		self.asset_size_storage = None
		self.nav = None
		self.personnel = None
		self.strategy = None
		self.attribute = None


	def _update_store_list(self, new_store_name):

		if new_store_name not in self.store_list:
			self.store_list.append(new_store_name)
		else:
			print(new_store_name+" has been updated before.")


	############################################################
	################ Store Data Methods ########################
	############################################################


	def store_asset_size(self, asset_size):

		self._update_store_list("asset_size")

		self.asset_size_storage = asset_size

	def store_nav(self,nav):

		self._update_store_list("nav")

		self.nav = nav

	def store_personnel_info(self, personnel):

		self._update_store_list("personnel")

		self.personnel = personnel

	def store_strategy(self,strategy):

		self._update_store_list("strategy")

		self.strategy = strategy

	def store_attribute(self,attribute):

		self._update_store_list("attribute")

		self.attribute = attribute



class GeneralFeatureStorage:

	def __init__(self,unique_id,fund_id,update_time,update_flag):

		self.unique_id = unique_id
		self.fund_id = fund_id
		self.update_time = update_time
		self.update_flag = update_flag




class AssetSizeStorage(GeneralFeatureStorage):


	def __init__(self,unique_id,fund_id,update_time,update_flag,date,asset_size_series):

		super().__init__(unique_id,fund_id,update_time,update_flag)
		self.date = date
		self.asset_size_series = asset_size_series





class NAVStorage(GeneralFeatureStorage):

	def __init__(self,unique_id,fund_id,update_time,update_flag,date,nav):

		super().__init__(unique_id,fund_id,update_time,update_flag)
		self.date = date
		self.nav = nav
		self.cumulative_nav = None
		self.cumulative_nav_withdrawal = None
		self.is_high_or_low = None



	def store_cumulative_nav(self,cumulative_nav):

		self.cumulative_nav = cumulative_nav


	def store_cumulative_nav_withdrawal(self,cumulative_nav_withdrawal):

		self.cumulative_nav_withdrawal = cumulative_nav_withdrawal


	def store_is_high_or_low(self,is_high_or_low):

		self.is_high_or_low = is_high_or_low





class StrategyStorage(GeneralFeatureStorage):

	def __init__(self,unique_id,fund_id,update_time,update_flag,strategy):

		super().__init__(unique_id,fund_id,update_time,update_flag)
		self.strategy = strategy
		self.substrategy = None


	def store_substrategy(self,substrategy):

		self.substrategy = substrategy






class AttributeStorage(GeneralFeatureStorage):


	def __init__(self,unique_id,fund_id,update_time,update_flag):

		super().__init__(unique_id,fund_id,update_time,update_flag)

		self.master_feeder_fund = None
		self.target_return_fund = None
		self.risk_buffer_fund = None
		self.umbrella_fund = None
		self.share_class = None
		self.seccom_hfcm = None
		self.futurecom_hfcm = None
		self.multi_advisor = None
		self.fee_class_a = None
		self.fee_class_other = None
		self.pro_class_m = None 
		self.pro_class_s = None
		self.creatorid = None























































