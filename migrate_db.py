import pandas as pd
import psycopg2
import os
from urllib.parse import urlparse

def migrate_excel_to_postgres():
    # Define the path to your Excel file
    excel_file = 'Dataset.xlsx'
    
    # Read the Excel file
    excel_data = pd.ExcelFile(excel_file)
    
    # Parse PostgreSQL URL
    db_url = urlparse(os.getenv('DATABASE_URL'))
    
    # Connect to PostgreSQL
    pg_conn = psycopg2.connect(
        dbname=db_url.path[1:],
        user=db_url.username,
        password=db_url.password,
        host=db_url.hostname,
        port=db_url.port
    )
    pg_cursor = pg_conn.cursor()
    
    # For each sheet in the Excel file
    for sheet_name in excel_data.sheet_names:
        # Load the sheet as a DataFrame
        df = excel_data.parse(sheet_name)
        
        # Get column names
        column_names = list(df.columns)
        print(column_names)
        
        # Create a table in PostgreSQL
        table_name = sheet_name.lower()  # Use sheet name as the table name
        column_definitions = ', '.join([f'"{col}" TEXT' for col in column_names])  # Assuming TEXT type for simplicity
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
        pg_cursor.execute(create_table_query)
        
        # Prepare insert query
        placeholders = ', '.join(['%s'] * len(column_names))
        column_str = ', '.join([f'"{col}"' for col in column_names])
        insert_query = f"INSERT INTO {table_name} ({column_str}) VALUES ({placeholders})"
        
        # Insert data into the table
        for _, row in df.iterrows():
            pg_cursor.execute(insert_query, tuple(row))
    
    # Commit and close
    pg_conn.commit()
    pg_cursor.close()

if __name__ == "__main__":
    migrate_excel_to_postgres()