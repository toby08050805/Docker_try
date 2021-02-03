from mysql_connector import mysqlConnect
from openpyxl import load_workbook
from time import sleep
import pandas as pd

if __name__ == '__main__':
    #connect=mysqlConnect('192.168.1.220','3309','covmo','covmo123','schema_pack_iii').getConnectcursor()
    #cur=connect.cursor()
    #cur.execute('show engines')
    #records = cur.fetchall()
    #print("count：", cur.rowcount)
    excel_path='./CovMo_LTE_5G_NSA_S20201105_R20201208.xlsx'
    usecols_raw=['#','Column Name','CH Data Type','CH Key']
    header=0
    sleep_time = 2
    um_retries = 4
    str_error = None
    for x in range(0,10):
        try:
            str_error = None
            df = pd.read_excel('./CovMo_LTE_5G_NSA_S20201105_R20201208.xlsx',engine='openpyxl',sheet_name='table_call_lte',nrows=21,usecols=usecols_raw,header=0)
        except Exception as str_error: 
            pass
        if str_error:
            sleep(sleep_time)  # wait before trying to fetch the data again
            sleep_time *= 2  # Implement your backoff algorithm here i.e. exponential backoff
        else:
            break
    print(df)