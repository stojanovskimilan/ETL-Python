import psycopg2

def drop_table(name):
    commands = ("""
    DROP TABLE """+name)
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



