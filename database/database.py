import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.db_file = "society_manager.db"
        self.conn = None
        self.create_tables()
    
    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            return self.conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        conn = self.create_connection()
        if conn is not None:
            # Staff table
            create_staff_table = """
            CREATE TABLE IF NOT EXISTS staff (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                salary REAL NOT NULL,
                join_date TEXT NOT NULL
            );"""

            # Residents table
            create_residents_table = """
            CREATE TABLE IF NOT EXISTS residents (
                flat_no TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                contact TEXT,
                join_date TEXT NOT NULL
            );"""

            # Bills table
            create_bills_table = """
            CREATE TABLE IF NOT EXISTS bills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bill_type TEXT NOT NULL,
                amount REAL NOT NULL,
                due_date TEXT NOT NULL,
                status TEXT NOT NULL
            );"""

            try:
                cursor = conn.cursor()
                cursor.execute(create_staff_table)
                cursor.execute(create_residents_table)
                cursor.execute(create_bills_table)
                conn.commit()
            except Error as e:
                print(f"Error creating tables: {e}")