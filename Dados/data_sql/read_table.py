import sqlite3
import pandas as pd

con = sqlite3.connect('./table/test.db')

# Lê direto com pandas
df = pd.read_sql_query("SELECT * FROM users", con)

print(df)

con.close()
