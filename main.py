#import pythonTest.mysql_connector as con
from pythonTest.mysql_connector import mysqlConnect as con
if __name__ == '__main__':
    #connect=con.mysqlConnect('192.168.1.220','3309','covmo','covmo123','schema_pack_iii').getConnectcursor()
    connect=con('192.168.1.220','3309','covmo','covmo123','schema_pack_iii').getConnectcursor()
    cur=connect.cursor()
    cur.execute('show engines')
    records = cur.fetchall()
    print("count：", cur.rowcount)