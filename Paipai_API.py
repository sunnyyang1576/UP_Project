import pandas as pd
import mysql.connector

rz_user = {'host': '119.23.156.67',
           'port':3306,
           'user':'data_user_yczctzb',
           'passwd':'L3dM$uIU6dvTeie1',
           'db':'rz_hfdb_core',
           'charset':'utf8'}


class PaiPai_HF_API:
    """
    This class initializes to extract information of the hedge funds from the PaiPai API.

    """

    def __init__(self, api_connection_info, _fund_id_list, _personnel_id_list):
        """
        This class has three attributes

        Attributes:
        ------------
        api_connection_info(dict): it contains the information needed to access the PaiPai API
        _fund_id_list(list(str)): it contains the fund_id of the funds needed
        _personnel_id_list(list(str)): it contains the personnel_id of the personnels needed

        """
        self.api_connection_info = api_connection_info
        self._fund_id_list = _fund_id_list
        self._personnel_id_list = _personnel_id_list

    def get_fund_strategy(self):
        '''
        This function returns the strategy for a fund.

        :return: dataframe with fund_id, update time, index for substrategy, and index for strategy
        :rtype: dataframe
        '''
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
            return df
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    def get_fund_ret(self):
        """
        This function returns the return for a fund.

        :return: dataframe with fund_id, end date and return
        :rtype: dataframe
        """
        try:
            print(tuple(self._fund_id_list))
            conn=mysql.connector.connect(host=rz_user['host'],user=rz_user['user'],passwd=rz_user['passwd'],db=rz_user['db'],port=rz_user['port'])
            cur=conn.cursor()
            cur.execute("SELECT fund_id as fund_id,\
                CONVERT(REPLACE(end_date,'-','') ,SIGNED) AS end_date,\
                    ret_1m FROM rz_hfdb_core.pvn_fund_performance \
                    WHERE fund_id IN "+str(tuple(self._fund_id_list))+";")

            data=cur.fetchall()
            df=pd.DataFrame(data,index=None,columns=['fund_id','end_date','ret'])
            df['ret']=df['ret'].astype(float)
            return df
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    def get_aum(self):
        '''
        This function returns the asset under management for a fund.

        :return: dataframe with fund_id, fund asset size date, and fund asset size.
        :rtype: dataframe
        '''
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
            return df
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    def get_current_personnel_info(self):
        """
        This function returns the personnel information for a fund manager.

        :return: dataframe with personnel id, education degree, investment experience in years, and major.
        :rtype: dataframe
        """
        try:
            print(tuple(self._personnel_id_list))
            conn = mysql.connector.connect(host=rz_user['host'], user=rz_user['user'], passwd=rz_user['passwd'],
                                       db=rz_user['db'], port=rz_user['port'])
            cur = conn.cursor()
            cur.execute("SELECT personnel_id as personnel_id,\
                    education as education,\
                    investment_experience as investment_experience,\
                    major as major,\
                    strategy FROM rz_hfdb_core.pvn_personnel_info \
                    WHERE fund_id IN " + str(tuple(self._personnel_id_list)) + ";")

            data = cur.fetchall()
            df = pd.DataFrame(data, index=None, columns=['personnel_id', 'education', 'investment_experience','major'])
            return df
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()





#personnel=PaiPai_HF_API.get_current_personnel_info(['',''])
#print(personnel)

#ret=PaiPai_HF_API.get_fund_ret(['HF0000000G','HF00000008','HF00000009','HF0000000A','HF0000000B','HF0000000C','HF0000000D'])
#export_fund_ret = ret.to_csv('ret.csv',index=None, header=True)
#print(ret)
