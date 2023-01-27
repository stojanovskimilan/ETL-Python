import psycopg2
import numpy as np
import psycopg2.extras as extras
import pandas as pd
  
conn = psycopg2.connect(host="localhost",database="postgres",user="postgres",password="12345678")
 
def execute_values(conn, df, table):
  
    tuples = [tuple(x) for x in df.to_numpy()]
  
    cols = list(df.columns)
    cols_renamed = []
    for col in cols:
        cols_renamed.append(col.replace(' ','_').replace('%','Percentage'))
    cols_renamed = ','.join(list(cols_renamed))
    # #SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols_renamed)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("The DataFrame is inserted")
    cursor.close()
    # print(query)
    # print(query)
    # # print(tuples)





