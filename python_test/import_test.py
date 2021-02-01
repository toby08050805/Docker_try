from python_test import mysql_connector

if __name__ == '__main__':
    connect=mysqlConnect('192.168.1.220','3309','covmo','covmo123','schema_pack_iii').getConnectcursor()
    cur=connect.cursor()
    cur.execute('show engines')
    records = cur.fetchall()
    print("count：", cur.rowcount)