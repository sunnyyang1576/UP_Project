from PaiPai_Data_Storage import (PaiPaiHFInstrument,
								 AssetSizeStorage,NAVStorage,StrategyStorage,AttributeStorage)

class DistributorController:

	def __init__(self,fund_id_list):
		"""
        Initialize the distributor controller with fund_id_list
		:param fund_id_list:
		"""
		self.fund_id_list = fund_id_list
		self.storage_dict = {}

		self.create_empty_HF_storage_instrument()
		# maybe we will consider to create_empty_HF_storage_instrument here, since next function
		# doesn't give any extra parameters, then do we still need "fund_id_list"? it seems like
		# self.fund_id_list is equivalent to the keys of self.storage_dict, so maybe we only need to
		# store the dictionary?
		# uncomment the following if you feel like to, and we could delete the "create_empty_HF_storage_instrument"
		# method.

		self.storage_dict = {}

		for fund_id in self.fund_id_list:
			self.storage_dict[fund_id] = PaiPaiHFInstrument(unique_id=None, fund_id=fund_id)

	def create_empty_HF_storage_instrument(self):

		# initialize empty PaiPaiHFInstrument and assign them to storage_dict

		for fund_id in self.fund_id_list:

			self.storage_dict[fund_id] = PaiPaiHFInstrument(unique_id=None, fund_id=fund_id)

			# print for testing issues? maybe we need to consider comment it out since it will have
			# a lot of messy outputs when we are trying to register all the instruments into our
			# collector
			print(fund_id+" is created.")
		print("All empty storage are created.")


	def distribute_asset_size(self,df,update_time):

		# initialize this distributor and update the df
		asset_distributor = AssetSizeDistributor(self.fund_id_list,update_time,df)

		for fund_id in self.fund_id_list:
			storage = asset_distributor.distribute_aum_data(fund_id)
			self.storage_dict[fund_id].store_asset_size(storage)
			print("Asset size of %s is stored."%(fund_id))




class SingleDistributor:

	def __init__(self,fund_id_list,update_time,df):

		self.fund_id_list = fund_id_list
		self.update_time = update_time
		self.df = df



	def fund_id_check(self):

		pass


	def columns_check(self,target_colume_name):

		pass






class AssetSizeDistributor(SingleDistributor):


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


















