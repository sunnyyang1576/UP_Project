import pandas as pd
import mysql.connector

rz_user = {'host': '119.23.156.67',
           'port':3306,
           'user':'data_user_yczctzb',
           'passwd':'L3dM$uIU6dvTeie1',
           'db':'rz_hfdb_core',
           'charset':'utf8'}


def get_fund_strategy(_fund_id_list):
    try:
        print(tuple(_fund_id_list))
        conn = mysql.connector.connect(host=rz_user['host'], user=rz_user['user'], passwd=rz_user['passwd'],
                                       db=rz_user['db'], port=rz_user['port'])
        cur = conn.cursor()
        cur.execute("SELECT fund_id as fund_id,\
            CONVERT(REPLACE(updatetime,'-','') ,SIGNED) AS updatetime,\
                    substrategy as substrategy,\
                    strategy FROM rz_hfdb_core.pvn_fund_strategy \
                    WHERE fund_id IN " + str(tuple(_fund_id_list)) + ";")

        data = cur.fetchall()
        df = pd.DataFrame(data, index=None, columns=['fund_id', 'updatetime', 'substrategy','strategy'])
        return df
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

strategy=get_fund_strategy(['HF0000000G','HF00000008','HF00000009','HF0000000A','HF0000000B','HF0000000C','HF0000000D'])
export_strategy = strategy.to_csv('strategy.csv',index=None, header=True)
print(strategy)


def get_fund_ret(_fund_id_list):
        try:
            print(tuple(_fund_id_list))
            conn=mysql.connector.connect(host=rz_user['host'],user=rz_user['user'],passwd=rz_user['passwd'],db=rz_user['db'],port=rz_user['port'])
            cur=conn.cursor()
            cur.execute("SELECT fund_id as fund_id,\
            CONVERT(REPLACE(end_date,'-','') ,SIGNED) AS end_date,\
                    ret_1m FROM rz_hfdb_core.pvn_fund_performance \
                    WHERE fund_id IN "+str(tuple(_fund_id_list))+";")

            data=cur.fetchall()
            df=pd.DataFrame(data,index=None,columns=['fund_id','end_date','ret'])
            df['ret']=df['ret'].astype(float)
            return df
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


ret=get_fund_ret(['HF0000000G','HF00000008','HF00000009','HF0000000A','HF0000000B','HF0000000C','HF0000000D'])
export_fund_ret = ret.to_csv('ret.csv',index=None, header=True)
print(ret)


def get_aum(_fund_id_list):
    try:
        print(tuple(_fund_id_list))
        conn = mysql.connector.connect(host=rz_user['host'], user=rz_user['user'], passwd=rz_user['passwd'],
                                       db=rz_user['db'], port=rz_user['port'])
        cur = conn.cursor()
        cur.execute("SELECT fund_id as fund_id,\
            CONVERT(REPLACE(fund_asset_size_date,'-','') ,SIGNED) AS fund_asset_size_date,\
                    fund_asset_size FROM rz_hfdb_core.pvn_fund_asset_size \
                    WHERE fund_id IN " + str(tuple(_fund_id_list)) + ";")

        data = cur.fetchall()
        df = pd.DataFrame(data, index=None, columns=['fund_id', 'fund_asset_size_date', 'fund_asset_size'])
        df['fund_asset_size'] = df['fund_asset_size'].astype(float)
        return df
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

aum=get_aum(['HF0000000G','HF00000008','HF00000009','HF0000000A','HF0000000B','HF0000000C','HF0000000D'])
export_aum = aum.to_csv('aum.csv',index=None, header=True)
print(aum)



def get_current_personnel_info(_personnel_id_list):
    try:
        print(tuple(_personnel_id_list))
        conn = mysql.connector.connect(host=rz_user['host'], user=rz_user['user'], passwd=rz_user['passwd'],
                                       db=rz_user['db'], port=rz_user['port'])
        cur = conn.cursor()
        cur.execute("SELECT personnel_id as personnel_id,\
                    education as education,\
                    investment_experience as investment_experience,\
                    major as major,\
                    strategy FROM rz_hfdb_core.pvn_personnel_info \
                    WHERE fund_id IN " + str(tuple(_personnel_id_list)) + ";")

        data = cur.fetchall()
        df = pd.DataFrame(data, index=None, columns=['fund_id', 'updatetime', 'substrategy','strategy'])
        return df
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

personnel=get_current_personnel_info(['',''])
print(personnel)
