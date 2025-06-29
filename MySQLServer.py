import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',             # Default MySQL user
            password=''              # Update with your actual password if needed
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except mysql.connector.Error as db_err:
                print(f"Failed to create database: {db_err}")
            finally:
                cursor.close()
                connection.close()

    except mysql.connector.Error as conn_err:
        print(f"Error while connecting to MySQL: {conn_err}")

if __name__ == '__main__':
    create_database()
