

from Series_DataManipulation import (SingleSeriesManipulation, MultipleSeriesManipulation)






class InstruManipulation:
	"""
	This class is used to manipulate the data stored in any certain instrument

	"""
	def __init__(self,instrument):

		self.__instrument = instrument
		self.__date = instrument.date



	def instru_type_change(self,target_instrument):

		pass


	def time_slicing(self,start,end):

		pass


	def time_aggregation(self,freq):

		pass




class SingleInstruManipulation(InstruManipulation):
	"""
	This class is used to perform data manipulation over general single series instrument. It also returns new single-series instrument.

	"""
	def __init__(self, instrument):
		"""This class inheritant from InstruManipulation. It also has additional attribute, series.

		Attribute:
		-----------

		series: pd.Series, from the price attribute of the instrument

		"""

		super(SingleInstruManipulation, self).__init__(instrument)
		self.series = instrument.price





	def instru_x_day_return(self,x_day=1,log_ret=True):
		"""This function calculates the x-day return of the single series instrument, and it also outputs an instrument.

		Args:
		    x_day: int
		    log_ret: boolean

		Returns:
		     Single_Asset_Instrument

		"""

		inter_obj = SingleSeriesManipulation(self.series,self.date)
		ret_series = inter_obj.x_day_return(x_day,log_ret)

		result_instru = Single_Asset_Instrument("Generation","return_series",self.__date,price=ret_series,ret=None)

		return result_instru



	def instru_lagged_series(self,lag):
		"""This function calculates the lagged series of a single series instrument, and it also outputs an instrument.

		Args:
		    lag: int

		Returns:
		     Single_Asset_Instrument

		"""


		pass


	def instru_cumulative_return(self):
		"""This function calculates the cumulative return of the price of the instrument.
		The origin is set to be 1

		Returns:
		    SingleSeriesManipulation

		"""


		pass



class HegdeFundManipulation(SingleInstruManipulation):


	def __init__(self,HF_instrument):

		super(HegdeFundManipulation, self).__init__(instrument)
		self.AUM = instrument.AUM



	def AUM_growth(self):
		"""This function calculates the change in AUM period by period across time.


		Returns:
		    SingleSeriesManipulation

		"""

		pass





class MultipleInstruManipulation(InstruManipulation):

	def __init__(self,instrument):
		super(SingleInstruManipulation, self).__init__(instrument)
		self.__series_dic = instrument.performance
		self.__ticker_list = instrument.ticker_list







	def instru_spred_calculation(self,target_ticker_list,standard=False):
		"""




		"""

		inter_obj = MultipleSeriesManipulation(self.__series_dic,self.__ticker_list,self.__date)
		spread = inter_obj.spread_calculation(target_ticker_list,standard)
		name = "Spread "+target_ticker_list[0]+"/"+target_ticker_list[1]

		if standard:
			name = "Standard " + name

		result_instru = Single_Asset_Instrument("Generation",name,self.__date,price=spread,ret=None)

		return result_instru











		
		






















