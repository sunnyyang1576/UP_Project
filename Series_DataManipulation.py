
import pandas as pd
import numpy as np
from Instrument import Single_Asset_Instrument, Multiple_Asset_Instrument



class SingleSeriesManipulation:
	"""
	This class is used to conduct data cleaning or any manipulation over a single time series data.
	It take in a series and outputs a series.

	"""

	def __init__(self,series,date):
		"""
		This class has two major attributes

		Attributes:
		------------

		series: pd.Series, the target time series
		date: pd.Series(datetime), the date corresponding to the the target series.

		"""
		series.index = date
		self.series = series
		self.date = date



    #############################################################################
    ################### Direct Manipulation no return ###########################
    #############################################################################


	def missing_value_manipulation(self,method="drop",business=True):
		"""
		This methods cleans the missing value within the series.

		:param method: str, it indicates the method to use for missing value cleaning
		:nreturn: it updates the series directly

		"""
		if business:
			start_date = self.date[0]
			end_date = self.date[-1]
			new_date_index = pd.date_range(start_date,end_date,freq="B")
			new_series = self.series.reindex(new_date_index)
		else:
			new_series = self.series

		if method == "drop":
			new_series = new_series.dropna()
		elif method == "forward":
			new_series = new_series.fillna(method="ffill")
		elif method == "backward":
			new_series = new_series.fillna(method="bfill")
		else:
			print("Undefined Method")

		return new_series



	def format_conversion(self,final_format="float"):
		"""
		This method converts the series into the desired format.

		:param final_format: str

		"""

		pass


	#############################################################################
    ################### Indirect Manipulation with return #######################
    #############################################################################




	def x_day_return(self,x_day=1,log_ret=True):
		"""
		This calculates the x-day return of a series.

		:param x_day: int
		:param: log_ret: boolean
		:return: pd.Series

		"""
		series = self.series

		if log_return:
			series_t = np.log(series)
			series_t_n = series_t.shift(n)
			ret = series_t - series_t_n
		else:
			series_t_n = series.shift(n)
			ret = (series - series_t_n)/series_t_n

		
		return ret






	def lagged_series_calculation(self,target_series,lag):
		"""
		This returns the lagged series of the target series

		:param x_day: int
		:return: pd.Series

		"""

		lagged_series = target_series.shift(lag)
		

		return lagged_series



	def cumulative_return(self):
		"""This function calculates the cumulative return of the series.
		The origin is set to be 1

		Returns:
		    cumulative return series, pd.Series

		"""

		pass










class MultipleSeriesManipulation:
	"""
	This class is used to conduct data manipulation over a set of series.

	"""


	def __init__(self,series_dic,ticker_list,date):
		"""

		Attributes:
		------------
		series_dic: dict{pd.Series}
		ticker_list: list(str)
		date: pd.Series

		"""

		self.series_dic = series_dic
		self.ticker_list = ticker_list
		self.date = self.date



	def spread_calculation(self,target_ticker_list,standard=False):
		"""
		This method calculates the spread between two target time series.

		:param target_ticker_list: list(str), the ticker name of the targets
		:param standard: boolean, whether to standardize the spread between two series
		:return: pd.Series


		"""

		target_1 = target_ticker_list[0]
		target_2 = target_ticker_list[1]
		series_1 = self.series_dic[target_1]
		series_2 = self.series_dic[target_2]
		spread = series_1 - series_2

		if standard:
			spread = spread/(series_1 + series_2)

		return spread








class TermStructureManipulation(MultipleSeriesManipulation):
	"""
	This class is used to conduct data manipulation over the term structure type data.

	"""



	def __init__(self,series_dic,ticker_list,date,maturity):
		"""
		It has the same attributes as Multiple_Series_Manipulation with additional maturity attributes

		Attributes:
		------------
		series_dic: dict{pd.Series}
		ticker_list: list(str)
		date: pd.Series
		maturity: list(float)


		"""


		Multiple_Series_Manipulation.__init__(self,series_dic,ticker_list,date)
		self.maturity = maturity




	def forward_value_computation(self):
		"""
		This function calculates the forward rate across the term structue and all maturities.

		:return: Multiple_Asset_Instrument

		"""


		def fun(series_1,series_2,maturity_1,maturity_2):
			forward_series = (sample_series_1 * maturity_1 - sample_series_2 * maturity_2)/(maturity_1 - maturity_2)
			return forward_series

		maturity_list = self.maturity
		term_struct_dict = self.series_dic

		forward_dict = {}
		name_list = []

		for index in range(1:len(maturity_list)):

			maturity_1 = maturity_list[index]
			maturity_2 = maturity_list[index-1]

			series_1 = term_struct_dict[str(maturity_1)]
			series_2 = term_struct_dict[str(maturity_2)]

			forward_rate = fun(series_1,series_2,maturity_1,maturity_2)
			name = str(maturity_1) + "-" + str(maturity_2)
			name_list.append(name)
			forward_dict[name] = forward_rate

		result_instru = Multiple_Asset_Instrument(name_list,forward_dict,self.date)
		return result_instru






























		













		






























