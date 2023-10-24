import os
import pyodbc


url = os.environ['HOST']
database = os.environ['DATABASE']
user = os.environ['USERNAME']
pwd = os.environ['PASSWORD']


connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={url};DATABASE={database};UID={user};PWD={pwd};TrustServerCertificate=yes'

conn = pyodbc.connect(connectionString)

SQL_QUERY = 'select * from tipo_productos'

cursor = conn.cursor()
cursor.execute(SQL_QUERY)


records = cursor.fetchall()
for r in records:
    print(f"{r.tipo_producto}\t{r.nom_tip_producto}")