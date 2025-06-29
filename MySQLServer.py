import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Yorktiles01@'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Failed to create database: {e}")
            finally:
                cursor.close()
                connection.close()

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

if __name__ == '__main__':
    create_database()
