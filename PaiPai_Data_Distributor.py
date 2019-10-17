from PaiPai_Data_Storage import (PaiPaiHFInstrument,
								 AssetSizeStorage,NAVStorage,StrategyStorage,AttributeStorage)

class DistributorController:

	def __init__(self,fund_id_list):
		"""
        Initialize the distributor controller with fund_id_list
		
		:param fund_id_list: list(str)
		"""
		self.fund_id_list = fund_id_list
		self.storage_dict = {}

		for fund_id in self.fund_id_list:
			self.storage_dict[fund_id] = PaiPaiHFInstrument(unique_id=None, fund_id=fund_id)




	def distribute_asset_size(self,df,update_time):
		"""
		This function is used to distribute the asset size dataframe into the corresponding hedge fund storage instrument

		:param update_time: str
		"""

		asset_distributor = AssetSizeDistributor(self.fund_id_list,update_time,df)

		for fund_id in self.fund_id_list:
			storage = asset_distributor.distribute_aum_data(fund_id)
			self.storage_dict[fund_id].store_asset_size(storage)
			print("Asset size of %s is stored."%(fund_id))




class SingleDistributor:
	"""
	This is the general distributor class. The general distributor takes in a dataframe and fund_id
	It then dissembles the dataframe based on the fund id, and it assignes the separate dataframe into
	the corresponding hedge fund storage instrument.

	"""

	def __init__(self,fund_id_list,update_time,df):

		self.fund_id_list = fund_id_list
		self.update_time = update_time
		self.df = df



	def fund_id_check(self):

		pass


	def columns_check(self,target_colume_name):

		pass






class AssetSizeDistributor(SingleDistributor):
	"""
	This distributor is used to distribute the asset size dataframe into the corresponding hedge fund storage.

	"""

	def __init__(self,fund_id_list,update_time,df):

		super().__init__(fund_id_list,update_time,df)

		self.fund_id_check()
		self.columns_check(["fund_asset_size","fund_asset_size_date"])




	def distribute_aum_data(self,fund_id):

		# get the corresponding asset size slice from the dataframe
		df = self.df

		sliced_df = df[df.fund_id==fund_id]
		date = sliced_df.fund_asset_size_date
		series = sliced_df.fund_asset_size
		temp_storage = AssetSizeStorage(unique_id=None,
										fund_id=fund_id,
										update_time=self.update_time,
										update_flag=True,
										date=date,
										asset_size_series=series)
		return temp_storage





		# initialize a AssetSizeStorage object



		# return the object
















class RetDistributor(SingleDistributor):


	def __init__(self,fund_id_list):

		super().__init__(fund_id_list,update_time)





class StrategyDistributor(SingleDistributor):

	def __init__(self,fund_id_list):

		super().__init__(fund_id_list,update_time)


















