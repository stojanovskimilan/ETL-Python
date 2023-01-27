import psycopg2

def create_table(name):
    commands = ("""
    CREATE TABLE """+name+""" ( 
	Store_No VARCHAR(50),
	Store TEXT,
	TY_Units INTEGER,
	LY_Units INTEGER,
	TW_Sales NUMERIC(20,2),
	LW_Sales NUMERIC(20,2),
	LW_Var_Percentage NUMERIC(3,2),
	LY_Sales NUMERIC(20,2),
	LY_Var_Percentage NUMERIC(20,2),
	YTD_Sales NUMERIC(20,2),
	LYTD_Sales NUMERIC(20,2),
	LYTD_Var_Percentage NUMERIC(20,2)
	)
    """)
    conn = None
    try:
        
        # connect to the PostgreSQL server
        conn = psycopg2.connect(host="localhost",database="postgres",user="postgres",password="12345678")
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



