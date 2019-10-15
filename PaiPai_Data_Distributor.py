


from PaiPai_Data_Storage import (PaiPaiHFInstrument,
	AssetSizeStorage,NAVStorage,StrategyStorage,AttributeStorage)






class DistributorController:

	def __init__(self,fund_id_list):


		self.fund_id_list = fund_id_list
		self.storage_dict = {}


	def create_empty_HF_storage_instrument(self):

		# initialize empty PaiPaiHFInstrument and assigne them to storage_dict

		for fund_id in self.fund_id_list:

			self.storage_dict[fund_id] = PaiPaiHFInstrument(unique_id=None,fund_id=fund_id)
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


















