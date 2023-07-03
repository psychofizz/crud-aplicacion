import pymssql

def check_mssql_connection(server, port, username, password):
    try:
        conn = pymssql.connect(server=server, port=port, user=username, password=password)
        print("Connection to MSSQL server successful!")
        conn.close()
    except pymssql.Error as e:
        print("Error connecting to MSSQL server:", e)