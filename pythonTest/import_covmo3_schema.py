from modules.parserProductTeamFileClass import productTeamFile
from openpyxl import load_workbook
import pandas as pd

if __name__ == '__main__':    
    #excel_path='./schemaPackUpdate/covmo3/raw_table/CovMo_LTE_5G_NSA_S20201105_R20201208.xlsx'
    #usecols_raw=['#','Column Name','CH Data Type','CH Key']
    #df = pd.read_excel('./schemaPackUpdate/covmo3/raw_table/CovMo_LTE_5G_NSA_S20201105_R20201208.xlsx',engine='openpyxl',sheet_name='table_call_lte',nrows=21,usecols=usecols_raw)
    #print(df)
    #print(df)
    COVMO = {'u': 'covmo', 'p': 'covmo123', 'h': '192.168.1.221', 'P': '3309', 'DB': 'schema_pack_iii'}