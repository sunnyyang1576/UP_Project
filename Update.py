import pandas as pd
import mysql.connector
from PaiPai_Data_Distributor import (DistributorController, SingleDistributor)


rz_user = {'host': '119.23.156.67',
           'port':3306,
           'user':'data_user_yczctzb',
           'passwd':'L3dM$uIU6dvTeie1',
           'db':'rz_hfdb_core',
           'charset':'utf8'}


class Update:

    def __init__(self,api_connection_info, _fund_id_list,_last_update_time):
        self._fund_id_list = _fund_id_list
        self._last_update_time = _last_update_time
        self.api_connection_info = api_connection_info


    def update_check(self):
        pass


    def update_strategy(self):
        try:
            print(tuple(self._fund_id_list))
            conn = mysql.connector.connect(host=rz_user['host'], user=rz_user['user'], passwd=rz_user['passwd'],
                                       db=rz_user['db'], port=rz_user['port'])
            cur = conn.cursor()
            cur.execute("SELECT fund_id as fund_id,\
                    CONVERT(REPLACE(updatetime,'-','') ,SIGNED) AS updatetime,\
                    substrategy as substrategy,\
                    strategy FROM rz_hfdb_core.pvn_fund_strategy \
                    WHERE fund_id IN " + str(tuple(self._fund_id_list)) + ";")

            data = cur.fetchall()
            df = pd.DataFrame(data, index=None, columns=['fund_id', 'updatetime', 'substrategy','strategy'])
            DistributorController.storage_dict = DistributorController.storage_dict + self._fund_id_list
            SingleDistributor.df = df
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    def update_ret(self):
        try:
            print(tuple(self._fund_id_list))
            conn = mysql.connector.connect(host=rz_user['host'], user=rz_user['user'], passwd=rz_user['passwd'],
                                           db=rz_user['db'], port=rz_user['port'])
            cur = conn.cursor()
            cur.execute("SELECT fund_id as fund_id,\
                 CONVERT(REPLACE(end_date,'-','') ,SIGNED) AS end_date,\
                     ret_1m FROM rz_hfdb_core.pvn_fund_performance \
                     WHERE fund_id IN " + str(tuple(self._fund_id_list)) + ";")

            data = cur.fetchall()
            df = pd.DataFrame(data, index=None, columns=['fund_id', 'end_date', 'ret'])
            df['ret'] = df['ret'].astype(float)
            DistributorController.storage_dict = DistributorController.storage_dict + self._fund_id_list
            SingleDistributor.df = df
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    def update_volatility(self):
        pass


    def update_drawdown(self):
        pass


    def update_VaR(self):
        pass


    def update_aum(self):
        try:
            print(tuple(self._fund_id_list))
            conn = mysql.connector.connect(host=rz_user['host'], user=rz_user['user'], passwd=rz_user['passwd'],
                                       db=rz_user['db'], port=rz_user['port'])
            cur = conn.cursor()
            cur.execute("SELECT fund_id as fund_id,\
            CONVERT(REPLACE(fund_asset_size_date,'-','') ,SIGNED) AS fund_asset_size_date,\
                    fund_asset_size FROM rz_hfdb_core.pvn_fund_asset_size \
                    WHERE fund_id IN " + str(tuple(self._fund_id_list)) + ";")

            data = cur.fetchall()
            df = pd.DataFrame(data, index=None, columns=['fund_id', 'fund_asset_size_date', 'fund_asset_size'])
            df['fund_asset_size'] = df['fund_asset_size'].astype(float)
            DistributorController.storage_dict = DistributorController.storage_dict + self._fund_id_list
            SingleDistributor.df = df

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

    def update_industry(self):
        pass

    def update_manager_info(self):
        try:
            print(tuple(self._personnel_id_list))
            conn = mysql.connector.connect(host=rz_user['host'], user=rz_user['user'], passwd=rz_user['passwd'],
                                       db=rz_user['db'], port=rz_user['port'])
            cur = conn.cursor()
            cur.execute("SELECT personnel_id as personnel_id,\
                    education as education,\
                    investment_experience as investment_experience,\
                    major FROM rz_hfdb_core.pvn_personnel_info \
                    WHERE fund_id IN " + str(tuple(self._personnel_id_list)) + ";")

            data = cur.fetchall()
            df = pd.DataFrame(data, index=None, columns=['personnel_id', 'education', 'investment_experience','major'])
            DistributorController.storage_dict = DistributorController.storage_dict + self._fund_id_list
            SingleDistributor.df = df
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()



