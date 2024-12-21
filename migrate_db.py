# migrate_db.py
import sqlite3
import psycopg2
from urllib.parse import urlparse
import os

def migrate_sqlite_to_postgres():
    # Connect to SQLite
    sqlite_conn = sqlite3.connect('db.sqlite3')
    sqlite_cursor = sqlite_conn.cursor()
    
    # Get all tables
    sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = sqlite_cursor.fetchall()
    
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
    
    # For each table
    for table in tables:
        table_name = table[0]
        if table_name != 'sqlite_sequence' and not table_name.startswith('django_'):
            # Get all data
            sqlite_cursor.execute(f"SELECT * FROM {table_name};")
            rows = sqlite_cursor.fetchall()
            
            if rows:
                # Get column names
                sqlite_cursor.execute(f"PRAGMA table_info({table_name});")
                columns = sqlite_cursor.fetchall()
                column_names = [col[1] for col in columns]
                
                # Create INSERT query
                placeholders = ','.join(['%s'] * len(column_names))
                column_str = ','.join(column_names)
                insert_query = f"INSERT INTO {table_name} ({column_str}) VALUES ({placeholders})"
                
                # Insert data
                for row in rows:
                    pg_cursor.execute(insert_query, row)
    
    # Commit and close
    pg_conn.commit()
    pg_cursor.close()
    pg_conn.close()
    sqlite_cursor.close()
    sqlite_conn.close()

if __name__ == "__main__":
    migrate_sqlite_to_postgres()