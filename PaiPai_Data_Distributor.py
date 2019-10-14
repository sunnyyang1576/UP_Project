









class DistributorController:

	def __init__(self,fund_id_list):


		self.fund_id_list = fund_id_list
		self.storage_dict = {}


	def create_empty_HF_storage_instrument(self):

		# initialize empty PaiPaiHFInstrument and assigne them to storage_dict

		pass



	def distribute_asset_size(self,distributor,df):

		# initialize this distributor and update the df




		# distribute the dataframe fund by fund
		# it needs to call the distribute function in single distributor
		# it also needs to call the update function in HF storage instrument






class SingleDistributor:

	def __init__(self,fund_id_list):

		self.fund_id_list = fund_id_list
		self.df = None

	def update_source_df(self,df):

		self.df = df


	def fund_id_check(self):

		pass


	def columns_check(self,target_colume_name):

		pass






class AssetSizeDistributor(SingleDistributor):


	def __init__(self,fund_id_list):

		super().__init__(fund_id_list)

		self.fund_id_check()
		self.columns_information_check(["fund_asset_size","fund_asset_size_date"])




	def distribute_aum_data(self,fund_id):

		# get the corresponding asset size slice from the dataframe



		# initialize a AssetSizeStorage object



		# return the object
















class RetDistributor(SingleDistributor):


	def __init__(self,fund_id_list):

		super().__init__(fund_id_list)





class StrategyDistributor(SingleDistributor):

	def __init__(self,fund_id_list):

		super().__init__(fund_id_list)

















