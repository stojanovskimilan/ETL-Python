# ETL-Python


1. Load the data from Excel Source

	
        load_data() -> returns pandas dataframe
		
2. Tranform the data


		transform_data() -> returns transformed dataframe
		
		1. Drop all NaN values.
		2. Drop the first rows.
		3. Get the column header names.
		4. Reset index and drop it.
		
3. Load the data into database
		
		
		connect() -> checks the connection with the PostgreSQL database.
		create_table() -> creates table with simmilar architecture like the source table.
		execute_values(connection_string, dataframe, tablename) -> inserts the transformed dataframe into the destination table (PostgreSQL table)



    

